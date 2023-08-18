import pyttsx3
from translate import Translator  

engine = pyttsx3.init()
  

engine.say("kya kar rahe ho")
translator= Translator(from_lang="english",to_lang="hi")
translation = translator.translate("Today is Tuesday")
print(translation)
engine.say(translation)
engine.runAndWait()