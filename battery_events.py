import psutil
from engine import *
def secs2hours(secs):
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)

# reading battery status
battery = psutil.sensors_battery()
bp = battery.percent
bcp = battery.power_plugged
bt = secs2hours(battery.secsleft)


def bevents():
    print(f"charge = {bp}, time left = {bt}, Charger Plugged-in = {bcp}")
    if bp <= 20:
        speak(
            f'Battery level is, {bp}  percent! System status: Critical! Time remaining: {bt}. We are now running on backup power! Charger Plugged-in: {bcp}')
    elif bp > 20 and bp <= 59:
        speak(
            f'Battery level is, {bp} percent! System status: Average!  Time remaining: {bt}. Charger Plugged-in: {bcp}')
    elif bp <= 10:
        speak('Battery level critical!  Time remaining: {bt}. Plugin power supply!')
    elif bp >= 60 and bp <= 99:
        speak(f'Battery level is, {bp} percent! System status: Good!  Time remaining: {bt}. Charger Plugged-in: {bcp}')
    elif bp == 100:
        speak(f'Battery is fully charged! Charger Plugged-in: {bcp}')