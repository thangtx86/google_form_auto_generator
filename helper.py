import random
import datetime
from vn_fullname_generator import generator
import unidecode


def save_to_file(file_path, content):
    """Helper function to save content to a file."""
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)
        print(f"Saved to {file_path}", flush=True)


def get_random_choice(options, num_choices=None):
    """Helper function to return a random choice or a sample."""
    if num_choices:
        return random.sample(options, k=num_choices)
    return random.choice(options)


def get_current_date():
    """Helper function to return the current date in 'YYYY-MM-DD' format."""
    return datetime.date.today().strftime('%Y-%m-%d')


def get_current_time():
    """Helper function to return the current time in 'HH:MM' format."""
    return datetime.datetime.now().strftime('%H:%M')


def random_answer_value(type_id, entry_id, options, required=False, entry_name=''):
    # fill random value except Short answer,paragraph,emailAddress (Text Input)
    # Dictionary to map type_id to their respective random value handling function
    type_handlers = {
        0: lambda: '' if not required else '',  # Short answer
        1: lambda: '' if not required else '',  # Paragraph
        2: lambda: get_random_choice(options),  # Multiple choice
        3: lambda: get_random_choice(options),  # Dropdown
        4: lambda: get_random_choice(options, num_choices=random.randint(1, len(options))),  # Checkboxes
        5: lambda: get_random_choice(options),  # Linear scale
        7: lambda: get_random_choice(options),  # Grid choice
        9: lambda: get_current_date(),  # Date
        10: lambda: get_current_time(),  # Time
        18: lambda: get_random_choice(options),  # Rank
    }

    # Return the value from the corresponding handler, or empty string if not found
    return type_handlers.get(type_id, lambda: '')()


def generate_email(name, domain="gmail.com", include_dot=True, include_number=False):
    parts = name.split()
    last_name = parts[0].lower()
    first_name = parts[-1].lower()

    last_name = unidecode.unidecode(last_name)
    first_name = unidecode.unidecode(first_name)

    if include_dot:
        base_email = f"{last_name}.{first_name}"
    else:
        full_name = "".join(parts).lower()
        full_name = unidecode.unidecode(full_name)
        base_email = full_name

    if include_number:
        number = f"{random.randint(0, 99):02}"
        base_email += number

    email = f"{base_email}@{domain}"
    return email


def generate_random_fullname(gender: int):
    if gender == 1:
        return generator.generate(1)
    elif gender == 0:
        return generator.generate(0)
    else:
        return generator.generate(1)


def random_birth_year():
    return random.randint(1994, 2000)


def random_gender():
    options = ['Nam', 'Nữ']  # Loại bỏ 'Khác'
    return random.choice(options)


def random_short_answer():
    options = ['', 'N.A', 'NA', 'Không']  # Loại bỏ 'Khác'
    return random.choice(options)


def random_gender_1():
    options = [1, 0]
    return random.choice(options)


def random_element_na():
    elements = ["N.A", "Na", "Không", "Ko", ""]
    return random.choice(elements)


def random_element_exclude_last(elements):
    if len(elements) < 2:  # Đảm bảo danh sách có ít nhất 2 phần tử
        raise ValueError("Danh sách phải có ít nhất 2 phần tử.")
    return random.choice(elements[:-1])  # Loại phần tử cuối cùng bằng slicing


def get_random_reasons(reasons, n=1):
    if n == 1:
        return random.choice(reasons)  # Trả về 1 phần tử dưới dạng list
    elif n > len(reasons):
        raise ValueError("Số lượng phần tử cần chọn lớn hơn độ dài của danh sách!")
    else:
        return random.sample(reasons, n)
