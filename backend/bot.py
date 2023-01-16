import speech_recognition as sr
from gtts import gTTS
import pyttsx3, os

listener = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[0].id)


def voice_engine(text):
    # define variables
    file = "backend/file.mp3"

    # initialize tts, create mp3 and play
    tts = gTTS(text, lang='en', tld="com")
    tts.save(file)
    os.system("mpg123 " + file)


def ask(text, options=None):

    if options:
        for i, j in enumerate(options):
            voice_engine(f"{i+1}. {j}")
    command = listen_query(text)
    return command


def listen_query(text=""):
    try:
        if text:
            voice_engine(text)
        with sr.Microphone() as source:

            voice = listener.listen(source)
            command = listener.recognize_google(voice, language="en-US")
            try:
                command = command.lower()
            except:
                pass

            if 'bye' in command:
                print("Bye exitting")
                return 0
            return command
    except Exception as e:
        print(e)
        return 0
