import smtplib
import random
import datetime as dt

email = 'YOUR_SMPT_EMAIL'
password = "YOUR_SMPT_PASSWORD"

def send_mail(email_body):
    with smtplib.SMTP(host = "smtp.gmail.com", port = "587") as connection:
        connection.starttls()
        connection.login(user = email, password = password)
        connection.sendmail(
            from_addr = email, 
            to_addrs = "xyz@email", 
            msg = email_body
        )
    
with open("quotes.txt", "r", encoding="utf-8") as quotes:
    list_quotes = [quote.strip() for quote in quotes.readlines()]
    if dt.datetime.now().weekday() == 0:
        quote = random.choice(list_quotes)
        email_body = f"Subject:Monday Motivation!!\n\n{quote}"
        send_mail(email_body)