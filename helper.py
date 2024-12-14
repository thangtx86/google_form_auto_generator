import random
import datetime

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