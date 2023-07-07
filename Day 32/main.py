import smtplib
import random
import pandas
import datetime as dt
from login_data import my_email, my_password

now = dt.datetime.now()
today = (now.month, now.day)

data = pandas.read_csv("birthdays.csv")

birthdays = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthdays:
    birthday_boy = birthdays[today]
    num = random.randint(1, 3)
    file_path = f"letter_templates/letter_{num}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_boy["name"])

# ---Send Email--- #
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=birthday_boy["email"],
                            msg=f"Subject: Happy Birthday!!\n\n{contents}")
