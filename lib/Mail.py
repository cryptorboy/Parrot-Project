import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import MySQLdb
import webbrowser as web
import json

class mail():
    def __init__(self,receiver_email, message, subject):
        super(mail,self).__init__()
        self.receiver_email = receiver_email
        self.message = message
        self.subject = subject
        with open ('lib\load.json','r') as f:
            data = json.load(f)
            self.name = data['name']
    def send(self):
        try:
            db = MySQLdb.connect(host="localhost", user="pratik", password="pratik[21]",database='parotdata')
            cur = db.cursor()
            sql = f"select email,email_pass from users WHERE username = '{self.name}'"
            cur.execute(sql)
            data = cur.fetchone()
            sender_email = data[0]
            sender_password = data[1]
            print(f"{sender_email},{sender_password}")
            db.commit()
            db.close()
            # Set up email parameters
            smtp_server = "smtp.gmail.com"
            smtp_port = 587


            # Create message
            msg = MIMEMultipart()
            msg["From"] = sender_email
            msg["To"] = self.receiver_email
            msg["Subject"] = self.subject
            msg.attach(MIMEText(self.message, "plain"))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(sender_email, sender_password)
                server.send_message(msg)
            url = "https://mail.google.com/mail/u/0/#sent"
            web.open(url)
        except smtplib.SMTPResponseException:
            print(e)
            return True
        except Exception as e:
            print(e)

        def SearchEmail():
            db = MySQLdb.connect(host="localhost", user="pratik", password="pratik[21]",database='parotdata')
            cur = db.cursor()
            sql = f"select email,email_pass from users WHERE username = '{self.name}'"
            cur.execute(sql)
            data = cur.fetchone()
            sender_email = data[0]
            sender_password = data[1]
            print(f"{sender_email},{sender_password}")
            db.commit()
            db.close()



if __name__ == "__main__":
    send_email = mail('joananna9886@gmail.com', 'hsssssssss','kkkkkk')
    print(send_email.send())