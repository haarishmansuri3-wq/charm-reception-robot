from gtts import gTTS
import speech_recognition as sr
import vlc
import time
from led_control import led_on, led_off

def speak(text):
if not text.strip():
return

```
tts = gTTS(text=text, lang="en", slow=False)
tts.save("response.mp3")

player = vlc.MediaPlayer("response.mp3")
player.play()

while True:
    time.sleep(0.1)
    if not player.is_playing():
        break
```

def listen():
recognizer = sr.Recognizer()

```
with sr.Microphone() as source:
    print("Listening...")
    led_on()
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)

led_off()

try:
    print("Recognizing...")
    user_input = recognizer.recognize_google(audio).lower()
    print("You:", user_input)
    return user_input

except sr.UnknownValueError:
    print("Could not understand audio.")
    return ""

except sr.RequestError:
    print("Speech recognition service unavailable.")
    return ""
```
