import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize speech engine
engine = pyttsx3.init()

# Voice settings
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 170)

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        command = command.lower()

        print("You said:", command)
        return command

    except sr.UnknownValueError:
        speak("Sorry, I could not understand.")
        return ""

    except sr.RequestError:
        speak("Network error.")
        return ""

def open_website(name, url):
    speak(f"Opening {name}")
    webbrowser.open(url)

def tell_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {current_time}")

def tell_date():
    current_date = datetime.datetime.now().strftime("%d %B %Y")
    speak(f"Today's date is {current_date}")

def search_google(query):
    speak(f"Searching for {query}")
    webbrowser.open(f"https://www.google.com/search?q={query}")

def run_assistant():
    speak("Hello! I am your personal voice assistant.")

    while True:
        command = take_command()

        if "open google" in command:
            open_website("Google", "https://www.google.com")

        elif "open youtube" in command:
            open_website("YouTube", "https://www.youtube.com")

        elif "open github" in command:
            open_website("GitHub", "https://github.com")

        elif "open chatgpt" in command:
            open_website("ChatGPT", "https://chat.openai.com")

        elif "time" in command:
            tell_time()

        elif "date" in command:
            tell_date()

        elif "search" in command:
            query = command.replace("search", "")
            search_google(query)

        elif "hello" in command:
            speak("Hello! How can I help you?")

        elif "your name" in command:
            speak("I am your AI personal voice assistant.")

        elif "exit" in command or "stop" in command:
            speak("Goodbye!")
            break

        elif command != "":
            speak("Command not recognized.")

# Start assistant
run_assistant()