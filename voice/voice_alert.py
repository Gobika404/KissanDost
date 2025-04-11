### voice/voice_alert.py

python
import pyttsx3

def speak_alert(messages, language="en"):
    """
    Converts a list of messages into speech alerts.
    """
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speech rate
    engine.setProperty('volume', 1.0)  # Volume 0.0 to 1.0

    for msg in messages:
        print(f"Speaking: {msg}")
        engine.say(msg)

    engine.runAndWait()

