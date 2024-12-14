
# Automatically Fill and Submit Google Form

Automatically Fill and Submit Google Form
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
- [ ] **Submit multiple forms at once** by specifying the desired number of submissions.

## Prerequisites
- Python 3.x
- `requests` library (`pip install requests`)
- `vn_fullname_generator` library (randomly generates Vietnamese-style full names )
- `faker` library (random email)

# Getting Started
If you're looking to quickly fill and submit a Google Form with random data, or customize the script to autofill with your own data, feel free to jump straight to the AutoFill and Submit section.

However, if you're interested in learning the process of creating a Python script to automate form submissions, follow the steps below. For those who want to skip the manual inspection, you can use the form.py script to automatically generate the request body, as detailed in the Extract Information Automatically section.
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

 https://docs.google.com/forms/d/107JbdZnD0ntlHGDUe_PzsDcriMEcaPGN0wFw0HLXTvc/viewform

```
{
    # ---------------------------------------1---------------------------------------------
    # Question: Question 1
    # (Optional)
    #   Answers: ['Answer 1', 'Answer 2', 'Answer 3', 'Answer 4']
    "entry.1588477123": ""
,
    # ---------------------------------------2---------------------------------------------
    # Question: Question 2 (Write something)
    # (Optional)
    #   Validation Rule: any text
    "entry.592612042": ""
,
    # ---------------------------------------3---------------------------------------------
    # Question: Question 3 (paragraph)
    # (Optional)
    #   Validation Rule: any text
    "entry.2088709806": ""
,
    # ---------------------------------------4---------------------------------------------
    # Question: Question 4 (Checkbox)
    # (Optional)
    #   Answers: ['Option 1', 'Option 2', 'Option 3', 'Option 4']
    "entry.928024575": ""
,
    # ---------------------------------------5---------------------------------------------
    # Question: Question 5
    # (Optional)
    #   Answers: ['Opt 1', 'Otp 2', 'Otp 3']
    "entry.1878463051": ""
,
    # ---------------------------------------6---------------------------------------------
    # Question: Queston 6: Row 1
    # (Optional)
    #   Answers: ['Column  1', 'Column 2', 'Column 3', 'Column 4', 'Column 5']
    "entry.1762622840": ""
,
    # ---------------------------------------7---------------------------------------------
    # Question: Queston 6: Row 2
    # (Optional)
    #   Answers: ['Column  1', 'Column 2', 'Column 3', 'Column 4', 'Column 5']
    "entry.550872671": ""
,
    # ---------------------------------------8---------------------------------------------
    # Question: Queston 6: Row 3
    # (Optional)
    #   Answers: ['Column  1', 'Column 2', 'Column 3', 'Column 4', 'Column 5']
    "entry.384063441": ""
,
    # ---------------------------------------9---------------------------------------------
    # Question: Queston 6: Row 4
    # (Optional)
    #   Answers: ['Column  1', 'Column 2', 'Column 3', 'Column 4', 'Column 5']
    "entry.631424289": ""
,
    # ---------------------------------------10---------------------------------------------
    # Question: Queston 6: Row 5
    # (Optional)
    #   Answers: ['Column  1', 'Column 2', 'Column 3', 'Column 4', 'Column 5']
    "entry.1376268242": ""
,
    # ---------------------------------------11---------------------------------------------
    # Question: Question 8
    # (Optional)
    #   Validation Rule: YYYY-MM-DD
    "entry.139813856": ""
,
    # ---------------------------------------12---------------------------------------------
    # Question: Email Address
    # (Required)
    #   Answers: email address
    "emailAddress": ""
,
    # ---------------------------------------13---------------------------------------------
    # Question: Page History
    # (Optional)
    #   Answers: from 0 to (number of page - 1)
    "pageHistory": "0,1"

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

URL = "https://docs.google.com/forms/d/107JbdZnD0ntlHGDUe_PzsDcriMEcaPGN0wFw0HLXTvc/viewform"
def manually_fill():
    payload = {
        'entry.1588477123': 'Answer 1',
        'entry.592612042': 'Sample',
        'entry.2088709806': 'Sample',
        'entry.928024575': ['Option 3', 'Option 2', 'Option 4', 'Option 1'],
        'entry.1878463051': 'Otp 3',
        'entry.1762622840': 'Column 3',
        'entry.550872671': 'Column 5',
        'entry.384063441': 'Column 5',
        'entry.631424289': 'Column 4',
        'entry.1376268242': 'Column 3',
        'entry.139813856': '2024-12-14',
        'emailAddress': 'email@email.com',
        'pageHistory': '0,1',
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
```
python form_submit.py 'https://docs.google.com/forms/d/e/<form-id>/viewform' -r
```

#### ⚙️ Customize the Script

You can easily modify the fill_form() function to enter the data you need. For example, if you want to fill in a random date and time:
```py


```

## 📝 Conclusion

With just a few lines of Python code, you can automate filling out and submitting Google Forms. Customize this script to fit your needs and save time on repetitive tasks!


*If there are any problems, please contact us via*

### Contact Me ☎️
Email: tranthang8696@gmail.com

Telegram: @thangtx86

Whashapp:  +(84) 886 620 246