import time
import random
import os
import win32clipboard
from textblob import TextBlob
from gtts import gTTS
from engine import *
from playsound import playsound
from pynput.keyboard import Key, Controller

def gspeak():

    # the read mode thing.
    rcmd = takeCommand().lower()
    keyboard = Controller()
    if 'start' in rcmd or 'reading' in rcmd or 'start reading' in rcmd or 'read' in rcmd:
        # copying selected text
        keyboard.press(Key.ctrl)
        keyboard.press('c')
        time.sleep(1)
        keyboard.release(Key.ctrl)
        keyboard.release('c')
        win32clipboard.OpenClipboard()
        # reading copied data
        rdata = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        ddata = TextBlob(rdata)
        # detecting the language of selected text.
        dlang = ddata.detect_language()
        if dlang=='en':
            playsound('istart.mp3')
            speak(rdata)
            playsound('istop.mp3')
        else:
            # pyttsx3 can't read some languages. so, here we use gTTs to read the detected language.
            speak("Sorry sir! I don't know the language you are selected! But, my friend friday can read it for you!")
            r1 = random.randint(1, 10000000)
            r2 = random.randint(1, 10000000)
            audout = str(r2) + "audio" + str(r1) + ".mp3"
            gtspeak = gTTS(text=rdata, lang=dlang, slow=False)
            gtspeak.save(audout)
            playsound('istart.mp3')
            playsound(audout)
            playsound('istop.mp3')
            os.chmod(audout, 0o777)
            os.remove(audout)
    else:
        # repeating if there is an error.
        speak("I didn't get that! say once more!" )
        gspeak()
