import speech_recognition as sr
import pyttsx3
from langdetect import detect
from translate import Translator  


# Initialize the speech recognizer
r = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set the voice assistant's voice
engine.setProperty('voice', 'en-us')  # You can choose different voices based on your system

# Function to convert text to speech
def speak(text, language):
    engine.setProperty('voice', language)  # Set the voice based on the language
    engine.say(text)
    engine.runAndWait()

# Function to capture voice input and convert it to text
def get_voice_input():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            # Use the speech recognition library to convert audio to text
            text = r.recognize_google(audio)
            print("You said:", text)
            return text
        except sr.UnknownValueError:
            print("Sorry, I didn't understand.")
        except sr.RequestError:
            print("Sorry, there was an issue with the speech recognition service.")

    return ""  # Return empty string if there was an error

# Function to greet the user
def greet(language):
    if language == 'en':
        speak("Hello! How can I assist you today?", 'en-us')
    elif language == 'fr':
        speak("Bonjour! Comment puis-je vous aider aujourd'hui?", 'fr-fr')
    elif language == 'es':
        speak("¡Hola! ¿En qué puedo ayudarte hoy?", 'es-es')
    # Add more greetings for different languages as needed

# Function to detect the language
def detect_language(text):
    try:
        return detect(text)
    except:
        return 'en'  # Default to English if language detection fails

# Function to translate the text
def translate_text(text, target_language):
    translator= Translator(from_lang="english",to_lang="fi")
    translation = translator.translate(text)
    return translation

# Main program loop
greet('en')  # Default to English greeting

while True:
    user_input = get_voice_input()

    if user_input.lower() == "exit":
        speak("Goodbye!", 'en-us')
        break

    # Detect the language of the user input
    user_language = detect_language(user_input)
    print(user_language)


    # Process user commands based on the detected language
    if "wikipedia" in user_input.lower():
        query = user_input.lower().replace("wikipedia", "")

        # Translate the query to English for Wikipedia search
        translated_query = translate_text(query, 'en')
        # search_wikipedia(translated_query)
    else:
        # Translate the user input to the detected language for the response
        translated_input = translate_text(user_input, user_language)
        speak("I'm sorry, I don't have information on that topic.", user_language)