import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pyjokes
import os
import pywhatkit
import time
from googletrans import Translator
import requests
import shutil

class Config:
    OPENWEATHER_API_KEY = "1a45e0667b1074687306201df0cf198f"
    DEFAULT_CITY = "Kurnool"
    APP_PATHS = {
        "chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    }
    VOICE_INDEX = 1

engine = pyttsx3.init()
engine.setProperty('rate', 170)
voices = engine.getProperty('voices')
try:
    engine.setProperty('voice', voices[Config.VOICE_INDEX].id)
except IndexError:
    print("Warning: Voice index not found. Using default.")

translator = Translator()

def speak(text):
    print("Fizzy: " + text)
    engine.say(text)
    engine.runAndWait()

def greet():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning! I am Fizzy, your personal assistant.")
    elif 12 <= hour < 18:
        speak("Good Afternoon! I am Fizzy, your personal assistant.")
    else:
        speak("Good Evening! I am Fizzy, your personal assistant.")
    speak("How can I help you?")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1.0
        r.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=8)
        except sr.WaitTimeoutError:
            print("No speech detected.")
            return ""
    try:
        command = r.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Please repeat.")
        return ""
    except sr.RequestError:
        speak("Could not connect to speech service. Check your internet.")
        return ""
    except Exception as e:
        speak(f"Error: {e}")
        return ""

def tell_time():
    speak(f"The time is {datetime.datetime.now().strftime('%I:%M %p')}")

def tell_joke():
    try:
        speak(pyjokes.get_joke())
    except Exception as e:
        speak(f"Couldn't fetch a joke: {e}")

def open_app(app_name):
    app_name = app_name.lower()
    if app_name == "camera":
        os.system("start microsoft.windows.camera:")
        speak(f"Opening {app_name}")
        return
    if app_name in Config.APP_PATHS:
        try:
            os.startfile(Config.APP_PATHS[app_name])
            speak(f"Opening {app_name}")
            return
        except Exception as e:
            speak(f"Error opening {app_name}: {e}")
            return
    exe_path = shutil.which(f"{app_name}.exe")
    if exe_path:
        os.startfile(exe_path)
        speak(f"Opening {app_name}")
    else:
        speak(f"Can't find {app_name}. Please configure it.")

def search_wikipedia(query):
    try:
        speak(f"Searching Wikipedia for {query}...")
        result = wikipedia.summary(query, sentences=2)
        speak(result)
    except Exception as e:
        speak(f"Error: {e}")

def play_song(song_name):
    if not song_name:
        speak("Please tell me the song name.")
        return
    speak(f"Playing {song_name} on YouTube")
    try:
        pywhatkit.playonyt(song_name)
    except Exception as e:
        speak(f"Couldn't play song: {e}")

def take_note():
    speak("What should I write?")
    note = take_command()
    if note:
        with open("note.txt", "a") as f:
            f.write(f"{datetime.datetime.now()} - {note}\n")
        speak("Note saved successfully!")
    else:
        speak("No note was taken.")

def set_reminder():
    speak("What should I remind you about?")
    reminder = take_command()
    speak("After how many seconds?")
    try:
        seconds = int(input("Enter seconds: "))
        speak(f"Reminder set for {seconds} seconds.")
        time.sleep(seconds)
        speak(f"Reminder: {reminder}")
    except:
        speak("Invalid time entered.")

def translate_to_english(text):
    if not text:
        speak("Please say something to translate.")
        return
    try:
        result = translator.translate(text, dest='en')
        speak("In English: " + result.text)
    except Exception as e:
        speak(f"Translation error: {e}")

def weather_info():
    city = Config.DEFAULT_CITY
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={Config.OPENWEATHER_API_KEY}&units=metric"
    try:
        data = requests.get(url).json()
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        speak(f"The temperature in {city} is {temp}°C with {desc}.")
    except Exception as e:
        speak(f"Couldn't get weather info: {e}")

def main():
    greet()
    while True:
        command = take_command()
        if "time" in command:
            tell_time()
        elif "joke" in command:
            tell_joke()
        elif "play" in command:
            play_song(command.replace("play", "").strip())
        elif "who is" in command or "what is" in command:
            search_wikipedia(command.replace("who is", "").replace("what is", "").strip())
        elif "note" in command:
            take_note()
        elif "remind" in command:
            set_reminder()
        elif "open" in command:
            open_app(command.replace("open", "").strip())
        elif "translate" in command:
            speak("What should I translate?")
            phrase = take_command()
            translate_to_english(phrase)
        elif "weather" in command:
            weather_info()
        elif "stop" in command or "exit" in command or "goodbye" in command:
            speak("Okay, see you later!")
            break
        elif command:
            speak("I'm still learning that command.")

if __name__ == "__main__":
    main()
