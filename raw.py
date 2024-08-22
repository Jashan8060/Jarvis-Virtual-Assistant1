import pyautogui
import speech_recognition as sr
import pyttsx3
import time
import pyperclip

engine = pyttsx3.init()
recognizer = sr.Recognizer()
microphone = sr.Microphone
def speech(c):
        engine.say(c)
        engine.runAndWait()

def recognize_speech_from_mic():
    """
    Handles speech recognition from a microphone input.
    Keeps asking for input until successful.
    """
    global recognizer
    global microphone  
  
    while True:
            try:
                with sr.Microphone() as source:
                    recognizer.adjust_for_ambient_noise(source)
                    audio = recognizer.listen(source, timeout=2, phrase_time_limit=3)
                    text = recognizer.recognize_google(audio)
                    print(f"{text}")
                    return text
                
            except sr.UnknownValueError:
                speech("Please try again.")

            except sr.RequestError:
                speech("Please try again.")
                
            except sr.WaitTimeoutError:
                speech("Please try again.")

while True:
     recognize_speech_from_mic()