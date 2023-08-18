import webbrowser as web
import time
import keyboard
import pyautogui as pg

def whatsapp(name,message):
    name = name
    message = message

    # Compose the URL to open the chat with the recipient
    url = f'https://web.whatsapp.com/'

    # Open the chat with the recipient in WhatsApp Web
    web.open(url)

    # Wait for the chat to load
    time.sleep(10)

    pg.click(33,182)
    time.sleep(2)

    # keyboard.write(message)
    # Press Enter to send the message
    keyboard.write(name)
    time.sleep(1)
    keyboard.press('enter')
    time.sleep(1)
    keyboard.write(message)
    time.sleep(1)
    keyboard.press('enter')



if __name__=='__main__':
    whatsapp('9886949323', 'Hello, this is an automated message')


    import pyautogui
    import time

    # time.sleep(1)
    # while True:
    #     k = pyautogui.position()
    #     print(k)
