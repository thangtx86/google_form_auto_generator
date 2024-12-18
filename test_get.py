import google_form as gf
import form_submit as fs
import file_helper
import helper
import random
import json
import url_util
import os
import requests
import copy
import adjust_answer as ans

RESPONSE_PATH = "response.xlsx"


def test_get():
    gf.handle_google_form_submission(
        form_url=url_util.URL_GET,
        output="output.txt",
    )


def test_submit():
    fs.main(
        url=url_util.URL_GET
    )


def submit(url: str, data: any, callback=None):
    try:
        url = gf.transform_form_url_to_response_url(url)
        res = requests.post(url, data=data, timeout=5)

        if res.status_code == 200:
            edit_token = url_util.extract_token(res.text)
            data_copy = copy.deepcopy(data)
            if edit_token:
                data_copy['edit2'] = edit_token

            if callback:
                callback(data_copy, edit_token)
            return True
        else:
            print("Error!", res.status_code, "while submitting form", res.text)
            if callback:
                callback(None, None)
            return False

    except requests.RequestException as e:
        print("Request failed:", e)
        if callback:
            callback(None, None)
        return False


def handle_response(data, edit_token, data_result):
    if data:
        print(f"Form submitted successfully with token: {edit_token}")
        data_result.append(data)
    else:
        print("Form submission failed.")


def submit_func():
    counters = {'success': 0, 'fail': 0, 'total': 0}
    data_result = []
    file_path = RESPONSE_PATH
    payload_generator = fs.generate_payloads(url_util.URL_GET, False, ans.adjust_answer, 10)
    if os.path.exists(file_path):
        file_helper.delete_file_if_open(file_path)

    for payload in payload_generator:
        counters['total'] += 1

        account = payload['emailAddress']
        print(f'{counters["total"]}. {account} submitting to {url_util.URL_GET}')

        if submit(url=url_util.URL_GET, data=payload,
                  callback=lambda data, edit_token: handle_response(data, edit_token, data_result)):
            counters['success'] += 1
        else:
            counters['fail'] += 1

    print(len(data_result))
    file_helper.save_payloads_to_excel(data_result, filename=RESPONSE_PATH)
    print(f'Finished with {counters["total"]} submissions')
    print(f'Success: {counters["success"]}, Fail: {counters["fail"]}')


def update_answer(answer):
    #  payload = {'entry.1908571199': 'Trần Xuân Thắng', 'entry.28611126': 'truong.khue73@@gmail.com', 'entry.1818831264': '', 'entry.1204198231': 'Male', 'entry.295633829': '35-44', 'entry.1463829470': '1-2 times', 'entry.598842785': ['Cultural/historical heritage', 'Rural areas', 'Mountains'], 'entry.2134336363': ['Spring', 'Summer', 'Winter', 'Autumn'], 'entry.143396356': 'Partner', 'entry.1720750409': 'My most .', 'entry.500480593': ['Public transportation', 'Airplane', 'Train', 'Car', 'Motorcycle'], 'entry.1512138449': ['Beautiful scenery', 'Delicious food', 'Local culture', 'Affordable costs'], 'entry.853858371': 'Adventure travel', 'entry.50875002': 'Da Nang .', 'entry.66152489': 'While Da Nang ', 'entry.1100270122': 'Under 5 million VND', 'entry.516363970': 'Neutral', 'entry.832965611': 'Very Important', 'entry.59865805': 'Very Important', 'entry.493972964': 'Neutral', 'entry.1010730600': 'Very Important', 'entry.1178398439': '2024-12-17', 'entry.1897488531': '19:14', 'entry.411302613': 'If ', 'entry.1608779174': '5', 'emailAddress': 'truong.khue73@@gmail.com', 'pageHistory': '0,1,2,3,4,5,6'}
    res = requests.post(url_util.url_update(url_util.URL_GET,
                                            "2_ABaOnufVWVQR0GHxNyZcNbud6mqtRaUTrglDyTtj8p7dQZzlUelfJBSq7ee16ixxeRuSWqY"),
                        data=answer, timeout=5)


#  submit(url=, data=payload)


if __name__ == "__main__":
    # update_answer()

    submit_func()
    # print(modify_url(URL_GET,"i28282"))
    # gf.handle_google_form_submission2(
    #    form_url= URL_GET,
    #     output="out",
    #     n=6
    # )
    # gf.handle_google_form_submission(url=URL_GET, output="output.txt")
