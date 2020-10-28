import speech_recognition as speech
from pynput.keyboard import Key, Controller
import time
import pydirectinput

r = speech.Recognizer()
keyboard = Controller()

time.sleep(3)

while 1:
    time.sleep(0.3)

    with speech.Microphone() as source:
        audio_data = r.record(source, duration=5)
        print("Recognizing...")
        try:
            text = r.recognize_google(audio_data, language = "de-DE")
        except:
            text = ""

        print(text)

    if text:
        pydirectinput.keyDown('t')
        time.sleep(0.1)
        pydirectinput.keyUp('t')

        time.sleep(0.2)

        keyboard.type(text)

        time.sleep(0.2)

        pydirectinput.keyDown('enter')
        time.sleep(0.1)
        pydirectinput.keyUp('enter')