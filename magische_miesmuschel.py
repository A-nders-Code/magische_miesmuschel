import pyttsx3
import random

#VOICE

def say(sp):
    engine = pyttsx3.init()
    german_voice_id = 'de'
    engine.setProperty('voice', german_voice_id)
    engine.say(sp)
    engine.runAndWait()

ja_nein = random.randint(0,10)

if ja_nein >= 5:
    say("Ja das solltest du tun!")
else:
    say("Davon würde ich abraten!")