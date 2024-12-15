import argparse
import datetime
import json
import random
import requests
import google_form
import time
import helper
from vn_fullname_generator import generator

def fill_random_value(type_id, entry_id, options, required=False, entry_name=''):
    # fill random value except Short answer,paragraph,emailAddress (Text Input)
    # Dictionary to map type_id to their respective random value handling function
    type_handlers = {
        0: lambda: '' if not required else '',  # Short answer
        1: lambda: '' if not required else '',  # Paragraph
        2: lambda: helper.get_random_choice(options),    # Multiple choice
        3: lambda: helper.get_random_choice(options),    # Dropdown
        4: lambda: helper.get_random_choice(options, num_choices=random.randint(1, len(options))),  # Checkboxes
        5: lambda: helper.get_random_choice(options),    # Linear scale
        7: lambda: helper.get_random_choice(options),    # Grid choice
        9: lambda: helper.get_current_date(),             # Date
        10: lambda: helper.get_current_time(),            # Time
        18: lambda:helper.get_random_choice(options),    # Rank
    }

    # Return the value from the corresponding handler, or empty string if not found
    return type_handlers.get(type_id, lambda: '')()

def generate_request_body(url: str, only_required = False,adjust_data=None):
    ''' Generate random request body data '''
    data = google_form.handle_google_form_submission(
        url,
        only_required = only_required,
        auto_fill_func = fill_random_value,
        output = "return",
        include_comments = False
    )
    data = json.loads(data)
    if adjust_data:
        data = adjust_data(data)

    return data

def submit(url: str, data: any):
    ''' Submit form to url with data '''
    url = google_form.transform_form_url_to_response_url(url)
    print("Send request to", url)
    res = requests.post(url, data=data, timeout=5)
    if res.status_code != 200:
        print("Error!", res.status_code, "while submitting form", res.text)


## Refactor your data to submit form inside adjust_data
def adjust_data(data):
    gender_value = data.get('entry.1204198231', '').lower()
    name_field = 'entry.1908571199'
    gender_type = 1 if gender_value == 'Male' else 0
    data[name_field] = helper.generate_random_fullname(gender_type)
    
    if data[name_field]:
        email = helper.generate_email(name=data[name_field],domain="@gmail.com",include_dot=True,include_number=True)
        data['emailAddress'] = email
        data['entry.28611126'] = email
    data['entry.1720750409'] = "My most recent travel experience was a trip to Da Nang, Vietnam. I spent time exploring the beautiful beaches, visited the famous Marble Mountains, and enjoyed the delicious local cuisine, such as Mi Quang and Banh Xeo. The city was a perfect blend of modernity and traditional charm, with friendly locals and breathtaking landscapes."
    data['entry.50875002'] = "Da Nang has several strengths in the tourism industry. First, its strategic location, with proximity to historical sites like Hoi An and Hue, makes it an ideal base for tourists. The city also offers stunning beaches like My Khe Beach, which attract beach lovers and adventure seekers. Additionally, the hospitality and friendliness of the people, along with an expanding infrastructure, contribute to making Da Nang a popular destination for both domestic and international tourists."
    data['entry.66152489'] ="While Da Nang is a beautiful destination with a lot to offer, there are a few aspects of the tourism industry that could be improved. First, the traffic congestion, especially during peak tourist seasons, can be quite frustrating. The city's infrastructure is still developing, and road conditions or the lack of efficient public transportation can hinder the overall experience. Additionally, while the popularity of Da Nang has been rising, some tourist attractions could benefit from better management in terms of cleanliness and facilities. Finally, more focus on sustainable tourism practices would help preserve the natural beauty of the area for future generations. This response highlights some areas for improvement in a constructive way."
    data['entry.411302613'] = "If I had the chance, I would love to visit Japan. I’m fascinated by its rich culture, ancient temples, beautiful landscapes like Mount Fuji, and vibrant cities such as Tokyo and Kyoto. I would also love to experience the unique Japanese traditions, including tea ceremonies, and enjoy the cherry blossoms in spring."
    return data

def main(url, only_required = False):
    try:
        payload = generate_request_body(url, only_required = only_required,adjust_data=adjust_data)
        print("Payload:", payload, flush = True)
        #
        submit(url, payload)
        print("Done!!!")
    except Exception as e:
        print("Error!", e.message)

RUN_TOTAL = 1

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=" Autofill and Submit Google Form")
    parser.add_argument("url", help="url of the form")
    parser.add_argument("-r", "--required", action="store_true", help="Only submit required fields")
    parser.add_argument("-n", type=int, default=1, help="Number of times to run the form submission (default is 1)")
    args = parser.parse_args()
    for _ in range(args.n):
        main(
            url=args.url,
            only_required=args.required,
        )

      
