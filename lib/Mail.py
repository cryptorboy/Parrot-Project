import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import MySQLdb
import webbrowser as web
import json
import imaplib
import email
import os 
import sys
from email.header import decode_header

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
class mail():
    def __init__(self,receiver_email, message, subject):
        super(mail,self).__init__()
        self.receiver_email = receiver_email
        self.message = message
        self.subject = subject
        with open (resource_path('lib\load.json'),'r') as f:
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
            return True
        except Exception as e:
            print(e)

    def SearchEmail(self):
            db = MySQLdb.connect(host="localhost", user="pratik", password="pratik[21]",database='parotdata')
            cur = db.cursor()
            sql = f"select email,email_pass from users WHERE username = '{self.name}'"
            cur.execute(sql)
            data = cur.fetchone()
            email_id = data[0]
            id_password = data[1]
            print(f"{email_id},{id_password}")
            db.commit()
            db.close()

            imap_server = 'imap.gmail.com'
            imap_port = 993
            email_add = email_id
            email_password = id_password

            mail = imaplib.IMAP4_SSL(imap_server, imap_port)
            mail.login(email_add, email_password)
            mail.select('inbox')

            # Search for emails
            status, email_ids = mail.search(None, 'ALL')
            email_ids = email_ids[0].split()

            # Retrieve and print email content
            for email_id in email_ids:
                status, email_data = mail.fetch(email_id, '(RFC822)')
                raw_email = email_data[0][1]
                msg = email.message_from_bytes(raw_email)
                
                print('From:', msg['From'])
                print('Subject:', decode_header(msg['Subject'])[0][0])  # Decode subject if needed
                            
                print('---')


if __name__ == "__main__":
    send_email = mail('joananna9886@gmail.com', 'hsssssssss','kkkkkk')
    # print(send_email.send())
    send_email.SearchEmail()