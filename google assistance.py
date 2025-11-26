import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os
import pywhatkit
import pyjokes
from transformers import pipeline
import torch

# Fastest Model Loading (CPU optimised)
device = 0 if torch.cuda.is_available() else -1
chatbot = pipeline("text-generation", model="microsoft/DialoGPT-small", device=device)

#  Voice Init (faster response)
engine = pyttsx3.init()
engine.setProperty('rate', 165)  # slightly faster speech

def speak(text):
    print("Bot:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙 Listening...")
        r.adjust_for_ambient_noise(source, duration=0.3)  # less wait
        try:
            audio = r.listen(source, timeout=4, phrase_time_limit=5)  # faster limit
            return r.recognize_google(audio).lower()
        except:
            speak("Sorry,shivani please repet"
                  )
            return ""

def run_assistant():
    speak("Hi Shivani! I'm ready.")

    while True:
        cmd = listen()

        if any(w in cmd for w in ["exit", "stop", "bye"]):
            speak("Goodbye Shivani!")
            break

        elif "youtube" in cmd:
            speak ("sure  youtube is opening shivani!")
            webbrowser.open("https://youtube.com")
        elif "google" in cmd:
            speak ("sure google is opening shivani!")
            webbrowser.open("https://google.com")
        elif "play" in cmd:
            speak ("sure it is playing shivani!")
            pywhatkit.playonyt(cmd.replace("play", "").strip())
        elif "search" in cmd:
            speak ("sure it is searching shivani!")
            pywhatkit.search(cmd.replace("search", "").strip())
        elif "notepad" in cmd:
            speak ("sure  notepad  is opening shivani!")
            os.system("notepad")
        elif "calculator" in cmd: 
            speak ("sure calculator is opening shivani!")
            os.system("calc")
        elif "camera" in cmd:
            speak ("sure  camera is opening shivani!")
            os.system("start microsoft.windows.camera:")
        elif "whatsapp" in cmd:
            speak ("sure  whatsapp is opening shivani!")
            webbrowser.open("https://web.whatsapp.com")
        elif "joke" in cmd:
            speak ("sure  joke is opening shivani!")
            speak(pyjokes.get_joke())
        elif "date" in cmd: speak(f"Today is {datetime.date.today().strftime('%B %d, %Y')}")
        elif "time" in cmd: speak(f"It is {datetime.datetime.now().strftime('%I:%M %p')}")
        elif "lock" in cmd: os.system("rundll32.exe user32.dll,LockWorkStation")
        elif "shutdown" in cmd: os.system("shutdown /s /t 10")
        elif "restart" in cmd: os.system("shutdown /r /t 10")
        elif "word" in cmd: os.system("start winword")
        elif "excel" in cmd: os.system("start excel")
        elif "powerpoint" in cmd: os.system("start powerpnt")

        elif cmd:
            # Chatbot Response (faster, shorter text)
            response = chatbot(cmd, max_length=60, do_sample=True, top_k=50, temperature=0.7)[0]['generated_text']
            speak(response)

if __name__ == "__main__":
   run_assistant()
