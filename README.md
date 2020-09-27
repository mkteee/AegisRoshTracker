## AegisRoshTracker

### Tracks the aegis and rosh spawn when it falls and announces via TTS.

__How it works__
* Uses [pyautogui](https://pypi.org/project/PyAutoGUI/) to detect if rosh/aegis events happened in the event history of the game
* Checks if game is paused to stop the timer
* Checks if game is maximized (in case of alt-tab at pause)
* Checks if chat is open (in case rosh/aegis are still visible via chat)
* Roshan voice via [pyttsx3](https://pypi.org/project/pyttsx3/) and aegis via [playsound](https://pypi.org/project/playsound/)


__What to do__
* Download zip file (top right)
* Extract in your wanted location
* Run "aegis_rosh_tracker.exe" (if it doesn't work try run as administrator)
* Can be started at any time, will detect automatically if you are ingame
* Create shortcut if wanted
* If buggy you probably need to restart the application

__Dependencies__
* pyautogui, pyttsx3, playsound, pywin32, opencv-python
