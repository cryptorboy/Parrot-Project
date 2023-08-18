import speech_recognition as sr
from googletrans import Translator 
from body.Speak import winspeak as speak
 

def takeCommand():
        # text1 = ui.pr()
        # print(text1)
        # ui.cleartext()
        #   
        # import speech_recognition as sr

        # Initialize the recognizer
        r = sr.Recognizer()

        with sr.Microphone() as source:
            # Capture the audio input from the microphone
            print("Listening...")
            audio = r.listen(source,0,5)

        print("Recognition in progress...")

        try:
            # Perform speech recognition
            text = r.recognize_google(audio,language="hi")
            
            # Print the recognized text
            print("Recognized text:", text)
            
            
        except sr.RequestError:
            speak("Please check your internet connection")
            return "none"
        except Exception as e:
              return "none"
        return TranslateText(text)
    
    #This is translator that translate hinto english words
def TranslateText(text):
         try:
            line = str(text)
            translate = Translator()
            result = translate.translate(line)
            data = result.text
            return data
         except Exception as e:
               print(e)

if __name__ == "__main__":
      print(takeCommand())