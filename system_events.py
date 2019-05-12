from engine import *
import os
import datetime

def sysshutdown():

    ch = takeCommand().lower()

    if 'yes' in ch:
      speak('System shutting down in, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1')
      os.system("shutdown /s /t 1")
    elif 'no' in ch:
      speak('System shut down, terminated!')
    else:
        speak("I didn't get that! say once more!" )
        sysshutdown()

def sysreboot():

    ch = takeCommand().lower()
    if 'yes' in ch:
        speak('System restarting in, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1')
        os.system("shutdown /r /t 1")
    elif 'no' in ch:
        speak('System reboot, terminated!')
    else:
        speak("I didn't get that! say once more!" )
        sysreboot()
def ctime():
     strTime = datetime.datetime.now().strftime("%H houres and %M minutes")
     speak(f"Sir, the time is {strTime}")
