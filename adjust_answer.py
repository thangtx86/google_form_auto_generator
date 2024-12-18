import helper
import random


#Refactor your data to submit form inside adjust_data
def adjust_answer(data):
    gender_value = data.get('entry.1204198231', '').lower()
    name_field = 'entry.1908571199'
    gender_type = 1 if gender_value == 'Male' else 0
    data[name_field] = helper.generate_random_fullname(gender_type)

    if data[name_field]:
        email = helper.generate_email(name=data[name_field], domain="@gmail.com", include_dot=True, include_number=True)
        data['emailAddress'] = email
        data['entry.28611126'] = email
    data['entry.1720750409'] = "My most recent travel "
    data['entry.50875002'] = "Da Nang has several strengths in the tourism industry."
    data['entry.66152489'] = "While Da Nang is a beautiful destination with a lot to offer"
    data['entry.411302613'] = "If I had the chance, I would love to visit Japan."
    return data
