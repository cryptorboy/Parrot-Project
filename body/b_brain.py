from bardapi import Bard
import pyttsx3

import os
def speak(audio):
                engine = pyttsx3.init('sapi5')
                voices = engine.getProperty('voices')
                    # print(voices[1].id)
                engine.setProperty('voice', voices[1].id)
                rate = engine.getProperty('rate')   # getting details of current speaking rate
                # print (rate)                        #printing current voice rate
                engine.setProperty('rate', 175)     # setting up new voice rate

                engine.say(audio)
                engine.runAndWait()

os.environ["_BARD_API_KEY"] = "ZQgC5thJCOeuKJiY2GpNCd4kRU0EfR0bwXuKcFRVYiTD3qQkGxXmy-TA2OVeQtc9mOPr3A."
while True:
    message = input("Enter your prompt: ")
    responce = Bard().get_answer(str(message))['content']
    responce = responce.replace("Bard","Parrot")
    print(responce)
    speak(responce)