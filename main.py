import threading
from speech import listen, speak
from ai_response import get_gemini_response, clean_response
from video_player import play_video_in_window

def run_chatbot():
while True:
print("Waiting for activation...")
user_input = listen().strip()

```
    if user_input == "hello":
        speak("Hello, I am the reception robot at Sanskaar Academy.")
        in_conversation = True

        while in_conversation:
            user_input = listen().strip()

            if user_input == "exit":
                speak("Bye bye, have a good day.")
                in_conversation = False
            else:
                response = get_gemini_response(user_input)
                response = clean_response(response)
                speak(response)
```

if **name** == "**main**":
video_thread = threading.Thread(
target=play_video_in_window,
args=("assets/EXPRESSIONS.mp4",),
daemon=True
)

```
chatbot_thread = threading.Thread(target=run_chatbot)

video_thread.start()
chatbot_thread.start()

chatbot_thread.join()
```
