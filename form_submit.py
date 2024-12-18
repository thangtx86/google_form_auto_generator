import argparse
import datetime
import json
import random
import requests
import google_form
import time
import helper
from vn_fullname_generator import generator


def generate_payloads(form_url, only_required, adjust_data, repeat_count):
    # Generator to create each payload
    base_data = google_form.handle_google_form_submission(
        form_url,
        only_required=only_required,
        auto_fill_func=helper.random_answer_value,
        output="return",
        include_comments=False,
        repeat_count=repeat_count
    )
    object_list = [json.loads(payload) for payload in base_data]
    adjusted_object_list = [adjust_data(item) for item in object_list]
    return adjusted_object_list


def submit(url: str, data: any):
    ''' Submit form to url with data '''
    url = google_form.transform_form_url_to_response_url(url)
    # print("Send request to", url)
    res = requests.post(url, data=data, timeout=5)
    if res.status_code != 200:
        print("Error!", res.status_code, "while submitting form", res.text)


def main(url, only_required=False):
    try:
        payload = generate_payloads(url, only_required=only_required, adjust_data=adjust_data)
        print("Payload:", payload, flush=True)
        #
        # submit(url, payload)
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
