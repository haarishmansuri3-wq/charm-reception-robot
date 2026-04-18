# Charm Reception Robot

A Raspberry Pi based voice-interactive receptionist robot built using Python, speech recognition, Gemini API, gTTS, GPIO, and VLC.

## Features

* Voice activation using “hello”
* Speech-to-text using Google Speech Recognition
* AI-generated responses using Gemini
* Text-to-speech output using gTTS
* GPIO-controlled LED indication
* Animated eye-expression video playback
* Multi-threaded operation

## Hardware Used

* Raspberry Pi
* Microphone
* Speaker
* LED
* Display

## Technologies

Python, Raspberry Pi GPIO, gTTS, SpeechRecognition, VLC, Gemini API, Tkinter

## Project Structure

```text
main.py              # Main chatbot loop
speech.py            # Speech input and output
ai_response.py       # Gemini API integration
led_control.py       # GPIO LED control
video_player.py      # Animated eye display
```

## How to Run

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Create a `.env` file and add your Gemini API key:

```text
GEMINI_API_KEY=your_api_key_here
```

3. Run the program:

```bash
python main.py
```

## Future Improvements

* Wake-word detection (“Hello Charm”)
* Offline speech recognition
* More expressive robot face animations
* Local AI model support
