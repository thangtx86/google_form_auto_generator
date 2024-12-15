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


def generate_email(name, domain="example.com", include_dot=True, include_number=False):
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
