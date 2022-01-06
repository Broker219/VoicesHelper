import datetime
import pyttsx3


def speak(what):
    print(what)
    speak_engine.setProperty('rate', 150)
    speak_engine.setProperty('volume', 0.9)
    speak_engine.say(what)
    speak_engine.runAndWait()
    speak_engine.stop()


speak_engine = pyttsx3.init()

speak('На часах ' + datetime.datetime.now().strftime('%H:%M'))
