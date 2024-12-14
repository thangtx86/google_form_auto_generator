import argparse
import datetime
import json
import random
import requests
import google_form
import time
import helper
from faker import Faker
from vn_fullname_generator import generator

URL_T = "https://docs.google.com/forms/d/1WDtIHnM4-XxRJwzTd-LEc6MYPyRnZ4u07uh2IoJ5Nw0/viewform"


def generate_random_email():
    dummy = Faker()
    return dummy.email()


def fill_random_value(type_id, entry_id, options, required=False, entry_name=''):

    # Handle specific entry ID cases first
    if entry_id == 'emailAddress':
        return generate_random_email()
    
    # Handle special case for 'Short answer'
    if entry_name == "Short answer":
        return 'N.A'
    
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
    }

    # Return the value from the corresponding handler, or empty string if not found
    return type_handlers.get(type_id, lambda: '')()

def generate_request_body(url: str, only_required = False):
    ''' Generate random request body data '''
    data = google_form.handle_google_form_submission(
        url,
        only_required = only_required,
        auto_fill_func = fill_random_value,
        output = "return",
        include_comments = False
    )

    data = json.loads(data)
    # you can also override some values here
    return data

def submit(url: str, data: any):
    ''' Submit form to url with data '''
    url = google_form.transform_form_url_to_response_url(url)
    print("Submitting to", url)
    print("Data:", data, flush = True)
   
    res = requests.post(url, data=data, timeout=5)
    if res.status_code != 200:
        print("Error! Can't submit form", res.status_code)

def main(url, only_required = False):
    try:
        payload = generate_request_body(url, only_required = only_required)
        #
        submit(url, payload)
        print("Done!!!")
    except Exception as e:
        print("Error!", e.message)

RUN_TOTAL = 1

if __name__ == '__main__':
    for i in range(RUN_TOTAL):
        print(f"Run {i + 1}")
        main(url=URL_T)
        
      
