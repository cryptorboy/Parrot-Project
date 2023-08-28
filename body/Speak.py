# Windows based Voice

import pyttsx3
def winspeak(audio):
                engine = pyttsx3.init('sapi5')
                voices = engine.getProperty('voices')
                    # print(voices[1].id)
                engine.setProperty('voice', voices[1].id)
                rate = engine.getProperty('rate')   # getting details of current speaking rate
                # print (rate)                        #printing current voice rate
                engine.setProperty('rate', 175)     # setting up new voice rate

                engine.say(audio)
                engine.runAndWait()

#Chrome based Voice

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from lib import startexec

from time import sleep
class OnlineVoice:
        def __init__(self):
                self.Check()
        try:
                def Check(self):
                        try:
                                self.chrome_options = Options()
                                self.chrome_options.add_argument('--log-level=3')
                                self.chrome_options.headless = True
                                # self.Path = 'lib\\chromedriver.exe'
                                self.driver = webdriver.Chrome(options=self.chrome_options)
                                self.driver.maximize_window()
                                self.website = r"https://ttsmp3.com/text-to-speech/British%20English/"
                                self.driver.get(self.website)
                                self.ButtonSelection = Select(self.driver.find_element(by=By.XPATH,value='/html/body/div[4]/div[2]/form/select'))
                                self.ButtonSelection.select_by_visible_text('British English / Brian')
                        except Exception as e:
                                print("Your are not connected to internet.",e)
                                self.Check()

                def chmspeak(self,text):
                        self.parrot = startexec.Run_Class()
                        self.parrot.p(text)
                        self.lengthoftext = len(str(text))
                        if self.lengthoftext==0:
                                pass
                        else:
                                # print("")
                                # print(f"AI: {text}")
                                # print(lengthoftext)
                                self.data = str(text)
                                self.xpathofsec = '/html/body/div[4]/div[2]/form/textarea'
                                self.driver.find_element(By.XPATH,value=self.xpathofsec).send_keys(self.data)
                                self.driver.find_element(By.XPATH,value='//*[@id="vorlesenbutton"]').click()
                                self.driver.find_element(By.XPATH,value='/html/body/div[4]/div[2]/form/textarea').clear()

                                if self.lengthoftext>=30:
                                        sleep(4)
                                # elif lengthoftext>=40:
                                #         sleep(6)
                                # elif lengthoftext>=55:
                                #         sleep(8)
                                # elif lengthoftext>=70:
                                #         sleep(10)
                                # elif lengthoftext>=100:
                                #         sleep(13)
                                # if lengthoftext>=120:
                                #         sleep(14)
                                else:
                                        sleep(2)
        except Exception as e:
                print(e)

if __name__=='__main__':
        # winspeak("TranslucentBackground")
    o =OnlineVoice()
    o.chmspeak("I see that you're interested in the meaning of your name. According to my search results, Pratik means shadow; symbol in Hindi. It's a beautiful name with a rich meaning. I'm sure you're a very special person with a bright future ahead of you.")
    from Listen import takeCommand
    while True:
            takeCommand()