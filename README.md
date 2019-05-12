# JARVIS-DesktopAssistant
A simple python desktop assistant like jarvis.

## Installation

You need Python 3.7 + installed in your system.

Clone or download this repo. and copy  ```JARVIS-DesktopAssistant``` folder to your ```C``` partition.

Click start button and type ```cmd``` and press ```enter```.

Type

```cd C:\JARVIS-DesktopAssistant```

```pip install -r requirements.txt```

This will install the dependencies require to run the app.

### Required additional modules

Try to install PyAudio by typing ```pip install PyAudio``` on cmd. If you are getting any error, download PyAudio from [here]( http://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio?) and install with ```pip install PATH_TO_DOWNLOADED_FILE```.

Check your Google Chrome version and download ```chromedriver``` from [here](http://chromedriver.chromium.org/downloads) , and copy it to ```JARVIS-DesktopAssistant``` folder.

### Configuration

Open ```config.py``` in Python IDLE or Notepad++ , and edit the fields.

Open command window in JARVIS-DesktopAssistant folder and type ```python core.py```

or, simply run jarvisstarter.bat.

### Features and Commands

◼️ _hello jarvis (or the name you are given), hi, hey_ to start using jarvis.

◼️ You can set a name for your assistant. Check config.py.

◼️ Tell you about system status. Say _system power status_

◼️ Clear recycle bin. Say _clear bin_

◼️ You can shut down or restart your system. Say _shut down system, reboot system_

◼️ Play Music. Say _play music, stop music_

◼️ Open facebook and create a post. Say _open facebook_

◼️ Send mail. _send mail_

◼️ Read any text and any language. Say _read screen_

◼️ _what's the time_

◼️ _what's the weather, what is 10+2, what is a dog, etc;_

◼️ _wikipedia "your query"_

◼️ _open google, youtube, git hub, etc;_


## To Do

◼️ YouTube Download

◼️ Copy and Paste

◼️ Change music track

◼️ Search files on pc

◼️ Change wallpaper

### AutoStart

To start jarvis when syatem starts, create a shortcut of jarvisstart.bat and copy it to windows startup folder.

To start jarvis without window, create and copy the shortcut of jstart.vbs to windows startup folder.


