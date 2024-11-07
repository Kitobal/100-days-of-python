import smtplib
from config import my_email, my_password
class NotificationManager:

    def __init__(self):
        # Retrieve environment variables only once
        self.smtp_address = "smtp.gmail.com"
        self.email = my_email
        self.email_password = my_password
        self.connection = smtplib.SMTP(self.smtp_address)

    def send_emails(self, email_list, email_body):
        with self.connection:
            self.connection.starttls()
            self.connection.login(self.email, self.email_password)
            for email in email_list:
                self.connection.sendmail(
                    from_addr=self.email,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{email_body}".encode('utf-8')
                )
