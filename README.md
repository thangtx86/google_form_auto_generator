
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
- [x]  **Automatically generates the request body** using the efficient `form.py` script, streamlining the process.
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
Use the `extract_form.py` script to automatically extract information about the form fields. This script will help you gather the field IDs that you'll need for the next step.

```
python extract_form.py <form-url>
```

This will return the necessary field information and their corresponding IDs.

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
# sample
```


### 4. Run the Script

After writing the script, you can run the following command to automatically fill and submit the form:
```
python form_submit.py <form-url>
```
For example:

```
python form_submit.py 'https://docs.google.com/forms/d/e/<form-id>/formResponse'
```

#### ⚙️ Customize the Script

You can easily modify the fill_form() function to enter the data you need. For example, if you want to fill in a random date and time:
```py


```

## 📝 Conclusion

With just a few lines of Python code, you can automate filling out and submitting Google Forms. Customize this script to fit your needs and save time on repetitive tasks!

### Contact Me ☎️
Email: tranthang8696@gmail.com

Telegram: @thangtx86

Whashapp:  +(84) 886 620 246