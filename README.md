
# Automatically Fill and Submit Google Form

Have you ever felt that filling out Google Forms daily, or even hourly, is a tedious and time-consuming task? Especially when you only need to change a few simple values but have to repeat the process over and over again for a long time. I'm sure you've wondered: Is there a way to automate this task?

Well, absolutely! You can fully automate the process of filling out and submitting Google Forms without lifting a finger, all with just a simple Python script.

I've also felt frustrated with repetitive tasks before, as they not only reduce productivity but also drain your motivation. That's why I created a solution that helps both you and me save time and energy. With this tool, you can easily create a script to automatically fill out and submit Google Forms, using pre-defined data or even random data. The task will be completed quickly, leaving you with more time for more exciting things, like chatting with your crush or significant other.

Imagine this: every day when you need to fill out some report forms for work, all you have to do is click a button, and all the data will be automatically filled in and submitted without any effort from you. What's even better is that you can customize this script to only fill in the required fields, instead of filling everything out, saving you a lot of time.

In this guide, I'll show you how to create a Python script that automatically fills out and submits Google Forms. You won’t have to worry about opening each form and filling in the details manually anymore.

Let's get started!

## Table of Contents


## Features

- [x]   **Fully supports multi-page Forms**, making it easier to automate complex forms.
- [x]  **Compatible with Google Forms that collect email addresses**, automatically inputting responder data.
- [x]  **Automatically generates the request body** using the efficient `google_form.py` script, streamlining the process.
- [x]  **Auto-fills the form with customizable random values** and submits it, saving you time and effort.
- [x] **Submit multiple forms at once** by specifying the desired number of submissions.


## Prerequisites
- Python 3.x
- `requests` library (`pip install requests`)
- `vn_fullname_generator` library (randomly generates Vietnamese-style full names )
- `faker` library (random email)

# Getting Started

### 1. **Get the Google Form URL**
To submit data to a Google Form, you'll need the form's URL. Typically, the form URL looks like this:
```
https://docs.google.com/forms/d/e/<form-id>/viewform
```
To submit data, change the `viewform` part to `formResponse`:
```
https://docs.google.com/forms/d/e/<form-id>/formResponse
```

### 2. **Extract Form Information**
#### Automatically Extract Information
Use the `google_form.py` script to automatically extract information about the form fields. This script will help you gather the field IDs that you'll need for the next step.

```
python google_form.py <form-url>
```
Also, You can also use -o out.txt to extract data taken from google form into file format so you can visualize its data.
 *(python google_form.py <form-url> -o filepath.txt)*

This will return the necessary field information and their corresponding IDs.

#### For output Example (when run ```python google_form.py <form-url> -o output.txt```) with URL at below:

 ```python google_form.py https://docs.google.com/forms/d/1PS5LMEs-C0T2EkJmoEHbv-zhNhGwZO4RenWu7CXJGoA/viewform -o output.txt```

ex:

```
{
    # ---------------------------------------1---------------------------------------------
    # Question: Full Name
    # (Optional)
    #   Validation Rule: any text
    "entry.1908571199": ""
,
    # ---------------------------------------2---------------------------------------------
    # Question: Contact Email
    # (Required)
    #   Validation Rule: any text
    "entry.28611126": ""
,
    # ---------------------------------------3---------------------------------------------
    # Question: Gender
    # (Optional)
    #   Answers: ['Male', 'Female', 'Other']
    "entry.1204198231": ""
,
    # ---------------------------------------4---------------------------------------------
    # Question: Your Age Group
    # (Optional)
    #   Answers: ['Under 18', '18-24', '25-34', '35-44', 'Over 45']
    "entry.295633829": ""
,
    # ---------------------------------------5---------------------------------------------
    # Question: How many times do you travel per year?
    # (Optional)
    #   Answers: ['1-2 times', '3-5 times', 'More than 5 times']
    "entry.1463829470": ""
,
    # ---------------------------------------6---------------------------------------------
    # Question: What travel destinations would you like to visit in the future?
    # (Optional)
    #   Answers: ['Mountains', 'Beach', 'Modern city', 'Cultural/historical heritage', 'Rural areas']
    "entry.598842785": ""
,
    # ---------------------------------------7---------------------------------------------
    # Question: When do you usually plan your trips?
    # (Optional)
    #   Answers: ['Spring', 'Summer', 'Autumn', 'Winter', 'Not fixed']
    "entry.2134336363": ""
,
    # ---------------------------------------8---------------------------------------------
    # Question: Who do you usually travel with?
    # (Optional)
    #   Answers: ['Alone', 'Family', 'Friends', 'Partner', 'Crush']
    "entry.143396356": ""
,
    # ---------------------------------------9---------------------------------------------
    # Question: What was your most recent travel experience?
    # (Optional)
    #   Validation Rule: any text
    "entry.1720750409": ""
,
    # ---------------------------------------10---------------------------------------------
    # Question: What is your preferred mode of transportation when traveling?
    # (Optional)
    #   Answers: ['Airplane', 'Train', 'Car', 'Motorcycle', 'Public transportation']
    "entry.500480593": ""
,
    # ---------------------------------------11---------------------------------------------
    # Question: What is the most important factor when choosing a travel destination?
    # (Optional)
    #   Answers: ['Beautiful scenery', 'Local culture', 'Affordable costs', 'Delicious food', 'Close to nature', 'Good infrastructure', 'Engaging activities']
    "entry.1512138449": ""
,
    # ---------------------------------------12---------------------------------------------
    # Question: What type of travel do you prefer?
    # (Optional)
    #   Answers: ['Leisure travel', 'Adventure travel', 'Independent travel', 'Group tours', 'Business trips combined with leisure']
    "entry.853858371": ""
,
    # ---------------------------------------13---------------------------------------------
    # Question: What strengths do you think the tourism industry in Da Nang has?
    # (Optional)
    #   Validation Rule: any text
    "entry.50875002": ""
,
    # ---------------------------------------14---------------------------------------------
    # Question: What aspects of tourism in Da Nang are you dissatisfied with?
    # (Optional)
    #   Validation Rule: any text
    "entry.66152489": ""
,
    # ---------------------------------------15---------------------------------------------
    # Question: How much are you willing to spend on each trip?
    # (Optional)
    #   Answers: ['Under 5 million VND', '5-10 million VND', '10-20 million VND', 'Over 20 million VND']
    "entry.1100270122": ""
,
    # ---------------------------------------16---------------------------------------------
    # Question: How important are the following factors to you when traveling? Columns: Very Important, Important, Neutral, Not Important): Natural scenery
    # (Optional)
    #   Answers: ['Very Important', 'Important', 'Neutral', 'Not Important']
    "entry.516363970": ""
,
    # ---------------------------------------17---------------------------------------------
    # Question: How important are the following factors to you when traveling? Columns: Very Important, Important, Neutral, Not Important): Cost
    # (Optional)
    #   Answers: ['Very Important', 'Important', 'Neutral', 'Not Important']
    "entry.832965611": ""
,
    # ---------------------------------------18---------------------------------------------
    # Question: How important are the following factors to you when traveling? Columns: Very Important, Important, Neutral, Not Important): Service quality
    # (Optional)
    #   Answers: ['Very Important', 'Important', 'Neutral', 'Not Important']
    "entry.59865805": ""
,
    # ---------------------------------------19---------------------------------------------
    # Question: How important are the following factors to you when traveling? Columns: Very Important, Important, Neutral, Not Important): Safety
    # (Optional)
    #   Answers: ['Very Important', 'Important', 'Neutral', 'Not Important']
    "entry.493972964": ""
,
    # ---------------------------------------20---------------------------------------------
    # Question: How important are the following factors to you when traveling? Columns: Very Important, Important, Neutral, Not Important): Local food
    # (Optional)
    #   Answers: ['Very Important', 'Important', 'Neutral', 'Not Important']
    "entry.1010730600": ""
,
    # ---------------------------------------21---------------------------------------------
    # Question: When was the last time you traveled?
    # (Optional)
    #   Validation Rule: YYYY-MM-DD
    "entry.1178398439": ""
,
    # ---------------------------------------22---------------------------------------------
    # Question: What time of day do you usually start your trips?
    # (Optional)
    #   Validation Rule: HH:MM (24h format)
    "entry.1897488531": ""
,
    # ---------------------------------------23---------------------------------------------
    # Question: If you had the chance, which country would you like to visit?
    # (Optional)
    #   Validation Rule: any text
    "entry.411302613": ""
,
    # ---------------------------------------24---------------------------------------------
    # Question: Please rank the following factors in order of importance when choosing a travel destination (1 = most important, 5 = least important)
    # (Optional)
    #   Answers: ['1', '2', '3', '4', '5']
    "entry.1608779174": ""
,
    # ---------------------------------------25---------------------------------------------
    # Question: Email Address
    # (Required)
    #   Answers: email address
    "emailAddress": ""
,
    # ---------------------------------------26---------------------------------------------
    # Question: Page History
    # (Optional)
    #   Answers: from 0 to (number of page - 1)
    "pageHistory": "0,1,2,3,4,5,6"

}

```

#### Manually

If you prefer doing it manually, open the DevTools (F12) in your browser and inspect the form elements. Each field you need to fill will have a name="entry.id" attribute that corresponds to the field ID.

#### Note:

#### Email Field
- If the form requires an email input, ensure the `emailAddress` field is added to the form data.

#### Multi-Page Forms
- For forms with multiple pages, include the `pageHistory` field to track the pages visited.
- The `pageHistory` field should be a comma-separated list of page indices, starting from `0`.

#### Example
For a 6-page form, the `pageHistory` field should be as follows:
```json
"pageHistory": "0,1,2,3,4,5,6"

```

### 3. Write a Python Script to Fill Out the Form
Once you have the form field information, you can write a Python script to fill the form. Here's an example:

```py
import form_submit

URL = "https://docs.google.com/forms/d/1PS5LMEs-C0T2EkJmoEHbv-zhNhGwZO4RenWu7CXJGoA/viewform"
def manually_fill():
    payload = {
    'entry.1908571199': 'Trịnh Trần Phương Tuấn',
    'entry.28611126': 'trinhtranphuongtuan_5m@@gmail.com',
    'entry.1204198231': 'Male',
    'entry.295633829': '35-44',
    'entry.1463829470': '1-2 times',
    'entry.598842785': ['Mountains', 'Rural areas', 'Beach'],
    'entry.2134336363': ['Summer', 'Spring', 'Winter', 'Autumn'],
    'entry.143396356': 'Alone',
    'entry.1720750409': 'My most recent travel experience was a trip to Da Nang, Vietnam. I spent time exploring the beautiful beaches, visited the famous Marble Mountains, and enjoyed the delicious local cuisine, such as Mi Quang and Banh Xeo. The city was a perfect blend of modernity and traditional charm, with friendly locals and breathtaking landscapes.',
    'entry.500480593': ['Airplane', 'Car', 'Train', 'Public transportation', 'Motorcycle'],
    'entry.1512138449': ['Good infrastructure', 'Beautiful scenery', 'Local culture', 'Delicious food', 'Close to nature', 'Affordable costs'],
    'entry.853858371': 'Independent travel',
    'entry.50875002': 'Da Nang has several strengths in the tourism industry. First, its strategic location, with proximity to historical sites like Hoi An and Hue, makes it an ideal base for tourists. The city also offers stunning beaches like My Khe Beach, which attract beach lovers and adventure seekers. Additionally, the hospitality and friendliness of the people, along with an expanding infrastructure, contribute to making Da Nang a popular destination for both domestic and international tourists.',
    'entry.66152489': 'While Da Nang is a beautiful destination with a lot to offer, there are a few aspects of the tourism industry that could be improved. First, the traffic congestion, especially during peak tourist seasons, can be quite frustrating. The city's infrastructure is still developing, and road conditions or the lack of efficient public transportation can hinder the overall experience. Additionally, while the popularity of Da Nang has been rising, some tourist attractions could benefit from better management in terms of cleanliness and facilities. Finally, more focus on sustainable tourism practices would help preserve the natural beauty of the area for future generations. This response highlights some areas for improvement in a constructive way.',
    'entry.1100270122': 'Over 20 million VND',
    'entry.516363970': 'Important',
    'entry.832965611': 'Important',
    'entry.59865805': 'Neutral',
    'entry.493972964': 'Important',
    'entry.1010730600': 'Not Important',
    'entry.1178398439': '2024-12-15',
    'entry.1897488531': '15:40',
    'entry.411302613': 'If I had the chance, I would love to visit Japan. I’m fascinated by its rich culture, ancient temples, beautiful landscapes like Mount Fuji, and vibrant cities such as Tokyo and Kyoto. I would also love to experience the unique Japanese traditions, including tea ceremonies, and enjoy the cherry blossoms in spring.',
    'entry.1608779174': '2',
    'emailAddress': 'trinhtranphuongtuan_5m@@gmail.com',
    'pageHistory': '0,1,2,3,4,5,6'
}

    
    return payload

form_submit.submit(URL, manually_fill())
```


### 4. Run the Script

After writing the script, you can run the following command to automatically fill and submit the form:
```
python form_submit.py <form-url>
```
Additionally, if you only want to fill in the required fields and skip optional ones, you can use this command:

```
python form_submit.py <form-url> -r
```

For example:

```
python form_submit.py 'https://docs.google.com/forms/d/e/<form-id>/viewform'
```
or 
* Only submit required field *
```
python form_submit.py 'https://docs.google.com/forms/d/e/<form-id>/viewform' -r
```
or If you want the form submission count to meet your requirements, try adjusting it according to the suggestion below

```
python form_submit.py 'https://docs.google.com/forms/d/e/<form-id>/viewform' -n 10
```


#### ⚙️ Customize the Script

You can easily modify the custom fill form function to enter the data you need. For example, if you want to fill in a random date and time:
```py

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

```

## 📝 Conclusion

With just a few lines of Python code, you can automate filling out and submitting Google Forms. Customize this script to fit your needs and save time on repetitive tasks!


*If there are any problems, please contact us via*

### Contact Me ☎️
Email: tranthang8696@gmail.com

Telegram: @thangtx86

Whatsapp:  +(84) 886 620 246

Fb: https://www.facebook.com/thangtx86