# Fizzy 🪄 - A Python Voice Assistant

A simple yet powerful personal voice assistant built in Python. **Fizzy** can help you with a variety of tasks, from telling you the time to searching Wikipedia, all through voice commands.

## 🌟 Features

Fizzy comes with a range of capabilities to make your daily tasks easier:

  * **Greets you** based on the time of day.
  * **Tells the current time**.
  * **Tells a random joke** to lighten your mood.
  * **Plays music** on YouTube by name.
  * **Searches Wikipedia** for any query ("who is" or "what is").
  * **Opens applications** on your computer (e.g., "open chrome", "open camera").
  * **Takes and saves notes** to a `note.txt` file.
  * **Sets a reminder** and notifies you after a specified time.
  * **Provides weather updates** for a default city.
  * **Translates phrases** into English.

## 🛠️ Technologies & Libraries

This project is built with Python and utilizes several powerful libraries:

  * **Speech Recognition:** `SpeechRecognition`  
  * **Text-to-Speech:** `pyttsx3`
  * **Web Automation/Search:** `wikipedia`, `pywhatkit`
  * **Jokes:** `pyjokes`
  * **API Requests:** `requests`
  * **Translation:** `googletrans`
  * **System Interaction:** `os`, `shutil`

## 🚀 Setup and Installation

### 1. Prerequisites
  * Python 3.7+
  * A working microphone
  * Internet connection

### 2. Clone the Repository
```bash
git clone https://github.com/yourusername/fizzy-assistant
cd fizzy-assistant
```

### 3. Install Dependencies
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

`requirements.txt` content:
```txt
SpeechRecognition
pyttsx3
wikipedia
pyjokes
PyAudio
pywhatkit
googletrans==4.0.0-rc1
requests
shutil
```

### 4. Configuration
Update the `Config` class in `fizzy.py` with your:
- OpenWeatherMap API key
- App paths (for opening apps)
- Voice index preference

### 5. Run Fizzy
```bash
python fizzy.py
```

### Example Commands
* "Hello Fizzy"  
* "What time is it?"  
* "Tell me a joke"  
* "Play Believer by Imagine Dragons"  
* "Who is Albert Einstein?"  
* "Open Chrome"  
* "Take a note"  
* "Set a reminder"  
* "What's the weather like?"  
* "Translate cómo estás"  
* "Stop" or "Goodbye"

## 🤝 Contribute
1. Fork the repo  
2. Create a new branch  
3. Commit and push changes  
4. Open a Pull Request  

## 📜 License
Licensed under MIT License.
