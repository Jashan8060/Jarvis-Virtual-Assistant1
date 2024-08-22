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
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=2)
                    text = recognizer.recognize_google(audio)
                    speech(f"You said: {text}")
                    return text
                
            #Sorry, I did not understand that.    
            except sr.UnknownValueError:
                speech("Please try again.")
                
            #Sorry, there was an error with the speech recognition service. 
            except sr.RequestError:
                speech("Please try again.")
                
            #Listening timed out while waiting for phrase to start.
            except sr.WaitTimeoutError:
                speech("Please try again.")

def placetrade():

    #Open Trading view
    speech("Opening Trading view")
    pyautogui.click(x=775,y=738)

    #Sleep 2 sec
    time.sleep(2)
    g = "Sir do you want to buy or sell"
    speech(g)
    c = recognize_speech_from_mic()
    if "buy" in c.lower() or "kharido" in c.lower():
        pyautogui.click(x=201, y=125)
        time.sleep(2)
        speech("How many units")
        c = recognize_speech_from_mic()
        units = str(c)
        print(units)
        pyautogui.doubleClick(x=528, y=334)
        a = pyperclip.copy(units)
        b = pyperclip.paste()
        pyautogui.write(b)
        time.sleep(2)
        pyautogui.click(x=665,y=600)
                        
    elif "sell" in c.lower() or "becho" in c.lower():
        pyautogui.click(x=99, y=125)
        time.sleep(2)
        speech("How many units")
        c = recognize_speech_from_mic()
        units = str(c)
        pyautogui.doubleClick(x=528, y=334)
        a = pyperclip.copy(units)
        b = pyperclip.paste()
        pyautogui.write(b)
        time.sleep(2)
        pyautogui.click(x=665,y=600)


placetrade()