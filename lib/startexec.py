import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QMovie
import datetime
import webbrowser
import pyautogui
import time
import re
import speech_recognition as sr
from googletrans import Translator
import wikipedia
import keyboard as key





from Windows.iputy import Ui_Form
from body import Speak
from lib.WhasApp import whatsapp
from Windows.New_Start_ui import Ui_Start_ui
from lib.Openbrow import open_url,search,search_engines,popular_websites
from lib.Map import MyLocation,GoogleMap



s = Speak.OnlineVoice()
def speak(text):
     s.chmspeak(text)

# LoginFeatureLap
# from StartUi import Ui_StartExitFrom
# master
from Windows.Started import  Ui_StartedForm

def takeCommand():
        # Initialize the recognizer
        r = sr.Recognizer()

        with sr.Microphone() as source:
            # Capture the audio input from the microphone
            print("Listening...")
            ui.showlabel("listening")
            audio = r.listen(source,0,5)

        print("Recognition in progress...")

        try:
            # Perform speech recognition
            ui.showlabel("recognising")
            text = r.recognize_google(audio,language="hi")
            
            # Print the recognized text
            print("Recognized text:", text)
            
            
        except sr.RequestError:
            speak("Please check your internet connection")
            return "none"
        except Exception as e:
              return "none"
        text = TranslateText(text)
        ui.user(text)
        return text 
    #This is translator that translate hinto english words
def hotkey():
        r = sr.Recognizer() 
        with sr.Microphone() as source:
            print("Hotkey Listening...")
            audio = r.listen(source,0,5)
        print("Recognition in progress...")
        try:
            # Perform speech recognition
            text = r.recognize_google(audio,language="hi")
            
            print("Recognized text:", text)
            
        except sr.RequestError:
            speak("Please check your internet connection")
            return "none"
        except Exception as e:
              return "none"
        text = TranslateText(text)
        ui.user(text)
        return text 
def TranslateText(text):
         try:
            line = str(text)
            translate = Translator()
            result = translate.translate(line)
            data = result.text
            return data
         except Exception as e:
               print(e)

def wishMe():
            hour = int(datetime.datetime.now().hour)
            if hour >= 0 and hour < 12:
                speak(" Good Morning")

            elif hour >= 12 and hour < 18:
                speak(" Good Afternoon")

            else:
                speak(" Good Evening")

            speak("Hello, I am Parrot. How can I help you today.")

#------------------------------------Open Apllication Function----------
def Openanyapplication(Application):
        pyautogui.press('win')
        time.sleep(1)
        pyautogui.write(Application)
        time.sleep(2)
        pyautogui.press('enter')



class Mainexecution(QThread):
    def __init__(self):
        super(Mainexecution, self).__init__()
 
    def run(self):
        self.wakeup()
    

    def wakeup(self):
        while True:
            self.query1 = hotkey().lower()

            print(self.query1)
            open=["parrot"]
            for opencmd in open:
                if opencmd in self.query1:
                    self.Boom()
            if "exit" == self.query1:
                speak("All functions are exiting and an application also exiting!. Thank You.")
                sys.exit(app.exit())
                break

    def Boom(self):
        print("boom function")
        ui.showlabel("startlable")
        wishMe()

        while True:
            self.query = takeCommand().lower()
            print(self.query)

            #this function handles all commands
            self.taskexecuter(self.query)      

    def taskexecuter(self,query):
                
#---------------------------------------------opening browser----------------->>>
            if "open" in self.query:
                    website = query.replace("open", "").strip().lower()
                    try:
                        open_url(popular_websites[website])
                        speak(f"Opening {website}") 
                    except:
                        speak(f"Opening {website}")
                        Openanyapplication(website)



#------------------------------------------Send whatsapp message----------->>>
            elif "whatsapp" in self.query:
                
                 speak("Ok, Tell me their WhatsApp number or name .")
                 while True:
                    def Number():
                        num = takeCommand().lower()
                        num = num.replace(" ","")
                        num = re.findall("\d{10}",num)
                        return num
                    self.num = Number()
                    if not self.num:
                        speak("Repeate that again.")
                    else:
                        while True: 
                            self.num = self.num[0]
                            speak("What message do you want to send?")
                            self.msg = takeCommand().lower()
                            if "none" != self.msg:
                                whatsapp(self.num, self.msg)
                                break
                            else:
                                speak("Say that again.")
                        break

#--------------------------------------------Show Location-------------->>>>
            elif "location" in self.query:
                 speak("Checking your location")
                 state ,country = MyLocation()
                 speak(f"you are in {state},{country} now.")

#------------------------------------------------search Place----------->>>>
            elif "where is" in self.query:
                 try:
                    self.place = self.query.replace("where is","")
                    self.place = self.place.replace("is", "")
                    self.place = self.place.replace("tell", "")
                    self.place = self.place.replace("me", "")
                    self.place = self.place.replace("parrot", "")


                    print(self.place)
                    asnwer = GoogleMap(self.place)
                    speak(f"{self.place} is {asnwer} kilometers away from your location.")
                 except:
                      speak("say that again.")

            elif "close window" in self.query:
                 speak("closing recently opened window")
                 key.press_and_release("Alt+F4")




e = Mainexecution()
class MainexecutionWindow(QMainWindow):
    def run(self):
        # super(MainexecutionWindow, self).__init__()
        # self.ui = Ui_StartExitFrom()
        # self.ui.setupUi(self)
        # self.ui.startButton.clicked.connect(lambda x: self.startexecution())
        # self.ui.ExitButton.clicked.connect(lambda y:sys.exit(app.exit()))
        # self.show()
        # take input through keyboard window
        self.Form = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.Form)
        self.ui.pushButton.clicked.connect(lambda x: self.keyboardcommad())
        # self.Form.show()
        self.startexecution()
    def keyboardcommad(self):
         userinput = self.ui.lineEdit.text()
         return userinput
    def cleartext(self):
        self.ui.lineEdit.clear()
         
      
    def StartFrom(self):
        self.startFrom = QtWidgets.QWidget()
        self.startui = Ui_Start_ui()
        self.startui.setupUi(self.startFrom)
        self.startui.label.hide()
        self.startui.label_2.hide()
        self.startui.label_3.hide()
        self.startui.label_4.hide()
        self.startui.pushButton.hide()
        self.startui.listening_lable1.hide()
        self.startui.listening_lable2.hide()
        self.startui.recognising_lable.hide()
        self.startui.listening_text.hide()
        self.startui.label_5.hide()
        self.startui.parrot_lable.hide()
        self.startui.user_lable.hide()
        self.startFrom.show()
        self.Start_animation()

    def Start_animation(self):
          self.listen1 = QMovie("design\Project-Parot-assets\start-window-assets\Listening.....gif")
          self.startui.listening_lable1.setMovie(self.listen1)
          self.listen1.start()

          self.listen2 = QMovie("design\Project-Parot-assets\start-window-assets\Listening....gif")
          self.startui.listening_lable2.setMovie(self.listen2)
          self.listen2.start()

          self.recog = QMovie("design\Project-Parot-assets\start-window-assets\Recognising.....gif")
          self.startui.recognising_lable.setMovie(self.recog)
          self.recog.start()

    def showlabel(self,state):

        if state == "startlable":
            self.startui.recognising_lable.hide() 
            self.startui.label.show()
            self.startui.label_2.show()
            self.startui.label_3.show()
            self.startui.label_4.show()
            self.startui.pushButton.show()
            self.startui.listening_lable1.show()
            self.startui.listening_lable2.show()
            self.startui.parrot_lable.show()
            self.startui.user_lable.show()

        elif state == "listening":
             self.startui.label_5.hide()
             self.startui.recognising_lable.hide() 
             self.startui.listening_lable1.show()
             self.startui.listening_lable2.show()
             self.startui.listening_text.raise_()
             self.startui.listening_text.show()

        elif state == "recognising":
             self.startui.listening_text.hide()
             self.startui.listening_lable1.hide()
             self.startui.listening_lable2.hide()
             self.startui.recognising_lable.raise_()
             self.startui.recognising_lable.show()
             self.startui.label_5.raise_()
             self.startui.label_5.show()

    def parrot(self,message):
         
         self.startui.parrot_lable.setText(message)
    def user(self,message):
         self.startui.user_lable.setText(message)

    def closelabel(self):
        self.startui.label.hide()
        self.startui.label_2.hide()
        self.startui.label_3.hide()
        self.startui.label_4.hide() 
        self.startui.recognising_lable.hide()
        self.startui.label_5.hide()
        self.startui.parrot_lable.hide()
        self.startui.user_lable.hide()
        self.startui.pushButton.hide()
         
    def closec(self):
        sys.exit(app.exit())
        # self.closelabel()
         

    def startexecution(self):
        self.StartFrom()
        e.start()

app = QtWidgets.QApplication(sys.argv)
ui = MainexecutionWindow()

class  Run_Class:
     def run(self):
        ui.run()
        sys.exit(app.exec_())
     def p(self,text):
        ui.parrot(text)
     def u(self,text):
          ui.user(text)
        
if __name__ == "__main__":
    r =Run_Class()



