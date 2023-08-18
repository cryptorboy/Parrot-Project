import speech_recognition as sr
import pyautogui

# Initialize the recognizer with Google Cloud Speech-to-Text API
r = sr.Recognizer()

# Function to open an application
def open_application(application_name):
    try:
        # Replace "open" with the command you want to use to open applications
        if "open" in application_name:
            # Replace the application names and their corresponding commands
            if "calculator" in application_name:
                pyautogui.press('win')
                pyautogui.typewrite('calculator')
                pyautogui.press('enter')
            elif "notepad" in application_name:
                pyautogui.press('win')
                pyautogui.typewrite('notepad')
                pyautogui.press('enter')
            elif "browser" in application_name:
                pyautogui.press('win')
                pyautogui.typewrite('chrome')
                pyautogui.press('enter')
            else:
                print("Application not found!")
        else:
            print("Command not recognized!")
    except Exception as e:
        print(e)

# Function to listen for voice commands
def listen_for_commands():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            # Use the Google Cloud Speech-to-Text API for online recognition
            command = r.recognize_google(audio)
            print("You said:", command)
            open_application(command.lower())
        except sr.UnknownValueError:
            print("Unable to recognize speech!")
        except sr.RequestError as e:
            print("Recognition request failed; {0}".format(e))

# Main program loop
while True:
    listen_for_commands()
