# py_mailer
Python process to retrieve bash mail from /var/mail/$USER and email it to a specified email addr.

## Requirements
- Python 3+
- basic python packages normally shipped with python3.*
    - smtplib
    - email
    - os
    - subprocess
- gmail email address 
    - without two factor authentication

## Setup & Run
1. download file: `wget githuburl.com`
1. edit file and fill in:
    ```python
    mail_from = 'email_to_send_from@gmail.com'
    mail_passwd = 'gmail_passwd'
    mail_to = 'email_to_send_to@someemail.com'
    ```
1. run: `python3 py_mailer.py`