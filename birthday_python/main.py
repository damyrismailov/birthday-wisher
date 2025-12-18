import datetime as dt
import random
import smtplib
import pandas

# Replace these with your real email + app password in your local/PythonAnywhere copy
my_email = "your_email@example.com"
password = "your_app_password_here"

now = dt.datetime.now()
today = (now.month, now.day)

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]): data_row
                 for (index, data_row) in data.iterrows()}

if today in birthday_dict:
    birthday_person = birthday_dict[today]
    letters = random.randint(1, 3)
    with open(f"./letter_templates/letter_{letters}.txt") as lt:
        the_letter = lt.read()
        the_letter = the_letter.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday! \n\n{the_letter}"
        )
