import pyttsx3
import speech_recognition as sr
from playsound import playsound

def speak(audio):
    # the speak feature thing.
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    # print(voices[1].id)
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        playsound('UI/sounds/istart.mp3')
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        playsound('UI/sounds/istop.mp3')
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
     #  print(e)
        print("didn't get that!")
        return "None"
    return query