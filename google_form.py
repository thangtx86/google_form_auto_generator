import argparse
import json
import re
import requests
import helper
import constant

def transform_form_url_to_response_url(form_url: str):
    """Transform a Google Form URL to its corresponding response URL."""
    if '/viewform' in form_url:
        return form_url.replace('/viewform', '/formResponse')
    return form_url.rstrip('/') + '/formResponse'

def extract_variable_from_script_tag(variable_name: str, html_content: str):
    """Extract the value of a JavaScript variable embedded in HTML script tags."""
    pattern = re.compile(r'var\s+' + re.escape(variable_name) + r'\s*=\s*(.*?);', re.DOTALL)
    match = pattern.search(html_content)
    if match:
        try:
            return json.loads(match.group(1))  # Try to parse the variable value as JSON
        except json.JSONDecodeError:
            return match.group(1)  # Return raw string if JSON parsing fails
    return None

def retrieve_form_metadata(form_url: str):
    """Fetch metadata from a Google Form using its URL."""
    try:
        with requests.get(form_url, timeout=10) as response:
            response.raise_for_status()  # Raise an error for bad responses (e.g., 404 or 500)
            metadata = extract_variable_from_script_tag(constant.FB_PUBLIC_LOAD_DATA_, response.text)
            if metadata is None:
                print(f"No metadata found for URL: {form_url}")
            return metadata
    except requests.RequestException as e:
        print(f"Error fetching form metadata from {form_url}: {e}")
        return None

def parse_google_form_fields(form_url: str, include_only_required=False):
    """Parse fields from a Google Form URL into structured metadata."""
    response_url = transform_form_url_to_response_url(form_url)
    form_data = retrieve_form_metadata(response_url)
    # print(response_url)

    if not form_data or not form_data[1] or not form_data[1][1]:
        print("Unable to retrieve form fields. Login may be required.")
        return None

    form_fields = form_data[1][1]
    fields_metadata = process_form_fields(form_fields, include_only_required)

    page_count = count_page_fields(form_fields)
    fields_metadata = add_optional_metadata(fields_metadata, form_data, page_count)

    return fields_metadata

def process_form_fields(form_fields, include_only_required):
    """Process form fields and return parsed metadata."""
    fields_metadata = []

    for field in form_fields:
        if field[3] == constant.SESSION_ID:  # Skip session fields
            continue
        fields_metadata.extend(parse_field_metadata(field, include_only_required))  # Extend the list with parsed field data

    return fields_metadata

def parse_field_metadata(field, include_only_required):
    """Parse field metadata and return structured info."""
    field_name = field[1]
    field_type = field[3]

    return [
        {
            "id": sub_field[0],
            "container_name": field_name,
            "type": field_type,
            "required": sub_field[2] == 1,
            "name": ' - '.join(sub_field[3]) if (len(sub_field) > 3 and sub_field[3]) else None,
            "options": [(opt[0] or constant.ANY_TEXT) for opt in sub_field[1]] if sub_field[1] else None,
        }
        for sub_field in field[4]
        if not include_only_required or sub_field[2] == 1
    ]

def count_page_fields(form_fields):
    """Count page fields in the form."""
    page_count = 0
    for field in form_fields:
        if field[3] == constant.SESSION_ID:  # Skip session fields
            page_count += 1
    return page_count

def add_optional_metadata(fields_metadata, form_data, page_count):
    """Add optional metadata like email and page history."""
    if form_data[1][10][6] > 1:
        fields_metadata.append({
            "id": "emailAddress",
            "container_name": "Email Address",
            "type": "required",
            "required": True,
            "options": "email address",
        })
    if page_count > 0:
        fields_metadata.append({
            "id": "pageHistory",
            "container_name": "Page History",
            "type": "required",
            "required": False,
            "options": "from 0 to (number of page - 1)",
            "default_value": ','.join(map(str, range(page_count + 1)))
        })
    return fields_metadata

def autofill_form_fields_with_defaults(fields, auto_fill_func):
    """Autofill form fields using a custom fill algorithm."""
    for field in fields:
        if 'default_value' in field:
            continue

        # Remove ANY_TEXT from options using list comprehension
        options = [opt for opt in (field.get('options') or []) if opt != constant.ANY_TEXT]

        # Call the auto_fill_func only if no default_value exists
        field['default_value'] = auto_fill_func(
            field['type'], field['id'], options,
            required=field.get('required', False),  # Use `get` to avoid errors if 'required' doesn't exist
            entry_name=field.get('container_name', '')
        )

    return fields

def generate_submission_payload(fields, include_comments=True):
    """Create a JSON payload for form submission."""
    payload_parts = ["{"]

    for idx, field in enumerate(fields):
        # Add comments if necessary
        if include_comments:
            comment_lines = [
                    f"    # ---------------------------------------{idx+1}---------------------------------------------",
                    f"    # Question: {field['container_name']}{(': ' + field['name']) if field.get('name') else ''}",
                    f"    # {'(Required)' if field['required'] else '(Optional)'}",
                    f"    #   Answers: {field['options']}" if field['options'] else f"    #   Validation Rule: {define_validation_rule_for_field_type(field['type'])}",
]
            payload_parts.extend(comment_lines)
           

        # Add the actual data part
        default_value = json.dumps(field.get("default_value", ""), ensure_ascii=False)
        field_id = field["id"]
        field_key = f"entry.{field_id}" if field.get("type") != "required" else field_id
        
        payload_parts.append(f'    "{field_key}": {default_value}')

        if idx < len(fields) - 1:
            payload_parts.append(",")

    payload_parts.append("\n}")
#     footer = [
#                     f"    # ---------------------------------------------------------------------------------------",
#                     f"    # Thanks ",
#                     f"    # Author: ThangTX86",
#                     f"    # Email: tranthang8696@gmail.com",
#                     f"    # https://thangtx86.github.io  ",
#                     f"    # ---------------------------------------------------------------------------------------",
# ]
#     payload_parts.extend(footer)
    return "\n".join(payload_parts)

def define_validation_rule_for_field_type(field_type):
    """Return the expected input rule for a given field type."""
    validation_rules = {
        9: "YYYY-MM-DD",
        10: "HH:MM (24h format)"
    }
    return validation_rules.get(field_type, "any text")

def handle_google_form_submission(form_url, output="console", only_required=False, include_comments=True, auto_fill_func=None):
    """Main function to process Google Form submission."""
    fields = parse_google_form_fields(form_url, include_only_required=only_required)
    
    if not fields:
        return None
    
    if auto_fill_func:
        fields = autofill_form_fields_with_defaults(fields, auto_fill_func)

    payload = generate_submission_payload(fields, include_comments)
    # print("Payload:", payload, flush=True)
    
    output_handlers = {
        "console": lambda: print(payload),
        "return": lambda: payload,
        "file": lambda: helper.save_to_file(output, payload)
    }

    handler = output_handlers.get(output)

    if handler:
        return handler()
    # If output is not 'console' or 'return', save to file
    if output not in ["console", "return"]:
        file_path = "output.txt"  # Specify a default or dynamic file path here
        helper.save_to_file(file_path, payload)
    
    return None
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=" Autofill and Submit Google Form")
    parser.add_argument("url", help="url of the form")
    parser.add_argument("-o", "--output", default="console", help="Output destination (default: console)")
    parser.add_argument("-r", "--required", action="store_true", help="Only get required fields")
    parser.add_argument("-c", "--no-comment", action="store_true", help="Write comment in output")
    args = parser.parse_args()

    handle_google_form_submission(
        form_url=args.url,
        output=args.output,
        only_required=args.required,
        include_comments=not args.no_comment
    )
