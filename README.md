# Birthday Wisher

Small Python script that checks each day whose birthday it is and sends a personalised “Happy Birthday” email using text templates. It can be run manually or scheduled on PythonAnywhere to run automatically every day.

## Main features

- Stores people and their dates of birth in `birthday_python/birthdays.csv` with columns: `name,email,year,month,day`.
- Uses `datetime` to get today’s month and day and look for matching rows in the CSV.
- Builds a dictionary where the key is `(month, day)` and the value is the full row, so the lookup is simple and fast.
- If today’s date is found, picks one of the files in `birthday_python/letter_templates/letter_1.txt`, `letter_2.txt` or `letter_3.txt` at random.
- Replaces the `[NAME]` placeholder in the chosen template with the person’s real name from `birthdays.csv`.
- Sends the final text as an email via SMTP using `smtplib` and `starttls`.
- If there is no birthday today, the script exits without sending anything.

## What I learned

- Working with dates and times using `datetime`.
- Reading and filtering CSV data with `pandas`.
- Building dictionaries with tuple keys for quick lookups.
- Loading and modifying text templates from external `.txt` files.
- Sending emails from Python using `smtplib` and secure connections.
- Structuring a small automation project so it can be reused or scheduled.

## Project structure

- `birthday_python/main.py` – main script; reads `birthdays.csv`, chooses a template and sends the email.
- `birthday_python/birthdays.csv` – list of people and their dates of birth.
- `birthday_python/letter_templates/letter_1.txt` – first email template with `[NAME]`.
- `birthday_python/letter_templates/letter_2.txt` – second email template with `[NAME]`.
- `birthday_python/letter_templates/letter_3.txt` – third email template with `[NAME]`.

## How to run locally

1. Make sure you have Python 3 installed.
2. Install the required package with `pip install pandas`.
3. Open `birthday_python/birthdays.csv` and add your own data, for example:

   `name,email,year,month,day`  
   `Alice,alice@example.com,1995,5,12`  
   `Bob,bob@example.com,2000,10,3`

4. Open `birthday_python/main.py` and set your email configuration at the top of the file:

   `my_email = "your_email@example.com"`  
   `password = "YOUR_APP_PASSWORD"`

   If you are not using Gmail, also change the SMTP host and port in the `smtplib.SMTP(...)` line to match your provider.

5. From the project folder, run `python birthday_python/main.py`.

If today’s month and day match any row in `birthdays.csv`, the script will pick a random template, replace `[NAME]` with the person’s name and send a personalised birthday email. If there is no match, nothing is sent.

## How to schedule on PythonAnywhere

1. Go to `pythonanywhere.com` and create an account.
2. In the “Files” tab, create a folder, for example `/home/yourusername/birthday-wisher/`.
3. Upload the `birthday_python` folder (with `main.py`, `birthdays.csv` and `letter_templates`) into that directory.
4. Open a Bash console on PythonAnywhere, run:

   `cd /home/yourusername/birthday-wisher`  
   `python3 birthday_python/main.py`

   and check that the script runs without errors and can send an email.

5. In the “Scheduled tasks” section on PythonAnywhere, create a new daily task with the command:

   `python3 /home/yourusername/birthday-wisher/birthday_python/main.py`

After this, PythonAnywhere will run `main.py` automatically every day. On days where the current date matches a row in `birthdays.csv`, a personalised birthday email will be sent using one of the templates in `letter_templates`.
