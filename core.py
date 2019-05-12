import smtplib
import wikipedia
import winshell
from gspeak import *
from battery_events import *
from system_events import *
from fb import *
from web_events import *


def wishMe():

    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")
    speak('Starting system sir!')
    speak('Loading Dependencies!')

    speak("System is online!")
    bevents()
    speak(f'{ass_name} at your service sir!')

def sendEmail(to, content):
    # setting up email module
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('GMail_id', 'GMail_pass')
    server.sendmail('GMail_id', to, content)
    server.close()


def jarvisCore():

    while True:
        # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'open facebook' in query:
            fb()
            jarvis()
        elif 'hello' in query:
            speak('Sir!')
            jarvis()
        elif 'clear bin' in query:
            try:
                winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
                speak('Trash Cleared!')
            except Exception as e:
                speak('Bin is clean sir!')
            jarvis()
        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak(f"According to Wikipedia, {results}")
            jarvis()
        elif 'power status' in query:
            bevents()
            jarvis()
        elif 'shutdown system' in query or 'shutdown' in query:
            speak("System Shut Down Initiated! Are you sure sir?")
            sysshutdown()
            jarvis()
        elif 'reboot system' in query:
            speak("System Shut Down Initiated! Are you sure sir?")
            sysreboot()
            jarvis()
        elif 'what' in query or 'weather' in query or 'get' in query:
            try:
                speak('searching...')
                res = wclient.query(query)
                results = next(res.results).text
                speak(f'Wolfram Alpha says,{results}')

            except Exception as e:
                print(e)
                speak('Sorry sir! No data, available!')
            jarvis()
        elif 'open youtube' in query:
           yt()
           jarvis()
        elif 'open google' in query:
            ggl()
            jarvis()

        elif 'open github' in query:
            git()
            jarvis()

        elif 'play music' in query:
            os.system(f"start AIMP3.exe {music_dir}")
            jarvis()

        elif 'stop music' in query or 'top music' in query:
            os.system("TASKKILL /F /IM AIMP3.exe")
            jarvis()
        elif "what's the time" in query:
            ctime()
            jarvis()

        elif 'open utorrent' in query:
            os.system('start uTorrent.exe')
            jarvis()
        elif 'read' in query or 'read screen' in query or 'read it' in query:
            speak('Select the text to read, then say, Start reading!')
            gspeak()
            jarvis()

        elif 'send a mail' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = Email_rp
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir! I am not able to send this email")
            jarvis()

def jarvis():

    # trigger module. say jarvis, hello jarvis, or the name you are given.
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            query = query.lower()
            if f"hello {ass_name}" in query or f"hey {ass_name}" in query or f"hi {ass_name}" in query or ass_name in query or "hello" in query or "hi" in query or "hey" in query:
                jarvisCore()
                print(f"User said: {query}\n")
            print(f"User said: {query}\n")

        except Exception as e:
            print(e)
            print("didn't get that!")


if __name__ == "__main__":
    wishMe()
    jarvis()
