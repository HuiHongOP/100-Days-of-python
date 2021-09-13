import datetime as dt
import smtplib 
import random
import pandas as pd

#This only works with gmail
today = (dt.datetime.now().month, dt.datetime.now().day)
my_email = 'YourEmail'
password = "YourPW"

data = pd.read_csv("birthday.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path, mode = "r") as file:
        contents = file.read()
        contents = contents.replace("[NAME]",birthday_person['name'])
    with  smtplib.SMTP("64.233.184.108") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Birthday\n\n{contents}"
        )
