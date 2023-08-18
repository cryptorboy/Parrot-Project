import webbrowser
import time
import pyautogui

# Open WhatsApp Web in the default web browser
# webbrowser.open('https://web.whatsapp.com')

# Wait for WhatsApp Web to load
# time.sleep(10)

# Define the recipient's name or group name and the message
number = 9886949323
message = 'Hello, this is an automated message!'

# Compose the URL to open the chat with the recipient
url = f'https://web.whatsapp.com/send?phone=+91{number}&text={message}'

# Open the chat with the recipient in WhatsApp Web
webbrowser.open(url)

# Wait for the chat to load
time.sleep(10)

# Press Enter to send the message 
pyautogui.press('enter')