# This is a sample Python script.
import pyautogui
import time
import pyttsx3
from pyttsx3.drivers import sapi5
import datetime
from threading import Thread
from playsound import playsound

# time.sleep(3)
# iml = pyautogui.screenshot(region=(1230, 802, 70, 40))
# iml.save(r"C:\Users\Marvin\PycharmProjects\DotaIngameTracker\testImg.png")

# (region=(0, 420, 700, 400)) for feed based recognition
# (region=(850, 385, 220, 30)) for pause screen
# (region=(729, 940, 20, 65)) for detecting if ingame
# (region=(1230, 802, 70, 40)) for detecting chat
en_voice_id = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
roshan_timer_active = False
aegis_timer_active = False
game_paused = False
roshan_respawn_time = 480
roshan_respawn_range = 180
aegis_time = 300
playsound(r"resources\bounty_runes.mp3")


class TTS:

    tts = None

    def __init__(self):
        self.tts = pyttsx3.init()
        self.tts.setProperty('volume', 0.5)
        self.tts.setProperty('rate', 145)
        self.tts.setProperty('voice', en_voice_id)

    def start(self, text_):
        self.tts.say(text_)
        self.tts.runAndWait()


def roshan_timer(t):
    global roshan_timer_active
    while t > 0:
        if not game_paused:
            t -= 1
            if t == 120:
                a = datetime.datetime.now()
                tts = TTS()
                tts.start("Roshan may spawn in 2 minutes")
                del tts
                b = datetime.datetime.now()
                c = b - a
                t = t - round(c.total_seconds())
            elif t == 60:
                a = datetime.datetime.now()
                tts = TTS()
                tts.start("Roshan may spawn in 1 minute")
                del tts
                b = datetime.datetime.now()
                c = b - a
                t = t - round(c.total_seconds())
            elif t == 30:
                a = datetime.datetime.now()
                tts = TTS()
                tts.start("Roshan may spawn in 30 seconds")
                del tts
                b = datetime.datetime.now()
                c = b - a
                t = t - round(c.total_seconds())
        time.sleep(1)
    a = datetime.datetime.now()
    tts = TTS()
    tts.start("Roshan may spawn now")
    del tts
    b = datetime.datetime.now()
    c = b - a
    roshan_timer_active = False
    roshan_range_timer(roshan_respawn_range-round(c.total_seconds()))
    return


def roshan_range_timer(t):
    while t > 0:
        if roshan_timer_active:
            return
        if not game_paused:
            t -= 1
            if t == 120:
                a = datetime.datetime.now()
                tts = TTS()
                tts.start("Roshan will spawn in 2 minutes")
                del tts
                b = datetime.datetime.now()
                c = b - a
                t = t - round(c.total_seconds())
            elif t == 60:
                a = datetime.datetime.now()
                tts = TTS()
                tts.start("Roshan will spawn in 1 minute")
                del tts
                b = datetime.datetime.now()
                c = b - a
                t = t - round(c.total_seconds())
        time.sleep(1)
    tts = TTS()
    tts.start("Roshan has spawned now")
    del tts
    return


def aegis_timer(t):
    global aegis_timer_active
    while t > 0:
        if not game_paused:
            t -= 1
            if t == 240:
                a = datetime.datetime.now()
                playsound(r"resources\aegis4_min.mp3")
                b = datetime.datetime.now()
                c = b - a
                t = t - round(c.total_seconds())
            elif t == 180:
                a = datetime.datetime.now()
                playsound(r"resources\aegis3_min.mp3")
                b = datetime.datetime.now()
                c = b - a
                t = t - round(c.total_seconds())
            elif t == 120:
                a = datetime.datetime.now()
                playsound(r"resources\aegis2_min.mp3")
                b = datetime.datetime.now()
                c = b - a
                t = t - round(c.total_seconds())
            elif t == 60:
                a = datetime.datetime.now()
                playsound(r"resources\aegis1_min.mp3")
                b = datetime.datetime.now()
                c = b - a
                t = t - round(c.total_seconds())
            elif t == 30:
                a = datetime.datetime.now()
                playsound(r"resources\aegis30_sec.mp3")
                b = datetime.datetime.now()
                c = b - a
                print(c.total_seconds())
                t = t - round(c.total_seconds())
            elif t == 10:
                a = datetime.datetime.now()
                playsound(r"resources\aegis10_sec.mp3")
                b = datetime.datetime.now()
                c = b - a
                print(c.total_seconds())
                t = t - round(c.total_seconds())
        time.sleep(1)
    aegis_timer_active = False
    return


while 1:
    # If a pause is detected
    if pyautogui.locateOnScreen(r'resources\pause.png', region=(850, 385, 220, 30), grayscale=True, confidence=0.9) \
            is not None:
        print("Pause")
        game_paused = True
    # If the game is not focused
    elif pyautogui.locateOnScreen(r'resources\ingame.png', region=(729, 940, 20, 68), grayscale=True, confidence=0.9) \
            is None:
        print("Game not focused")
    elif pyautogui.locateOnScreen(r'resources\chat.png', region=(1230, 802, 70, 40),  grayscale=True, confidence=0.8) \
            is not None:
        print("Chat open")
    # If the game is focused and there is no pause
    else:
        if game_paused:
            game_paused = False
            time.sleep(3)
        # If Roshan kill gets detected and a spawn is impossible
        if pyautogui.locateOnScreen(r'resources\roshan.png', region=(0, 420, 700, 400), grayscale=True, confidence=0.9)\
                is not None and not roshan_timer_active:
            print("Start roshan timer")
            roshan_timer_active = True
            roshan_thread = Thread(target=roshan_timer, args=(roshan_respawn_time,))
            roshan_thread.start()
        # If Aegis gets detected and there currently is no aegis
        if pyautogui.locateOnScreen(r'resources\aegis.png', region=(0, 420, 700, 400), grayscale=True, confidence=0.9) \
                is not None and not aegis_timer_active:
            print("Start aegis timer")
            aegis_timer_active = True
            aegis_thread = Thread(target=aegis_timer, args=(aegis_time,))
            aegis_thread.start()
    time.sleep(1)
