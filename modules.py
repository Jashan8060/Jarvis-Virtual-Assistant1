# Import necessary libraries
import webbrowser as wb  # For opening URLs in a web browser
import requests  # For making HTTP requests
import pyttsx3  # For text-to-speech conversion
import speech_recognition as sr  # For speech recognition
import pyautogui  # For automating GUI interactions
import time  # For adding delays
import pyperclip  # For clipboard operations
import subprocess  # For running system commands
import sys  # For system-specific parameters

"""Dictionary with music song names and their corresponding YouTube URLs
Include more urls for more songs"""
musicLibrary ={
    "soch": "https://www.youtube.com/watch?v=E8rpY2FwKkY&pp=ygUEc29jaA%3D%3D",
    "perfect": "https://www.youtube.com/watch?v=2Vv-BfVoq4g&pp=ygUHcGVyZmVjdA%3D%3D",
    "friends": "https://www.youtube.com/watch?v=jzD_yyEcp0M&pp=ygUNZW5nbGlzaCBzb25ncw%3D%3D",
    "runaway":"https://www.youtube.com/watch?v=d_HlPboLRL8&pp=ygUGYXVyb3Jh"
}

# Define your API key for the news API
news_api_key = "faa878d35a854d73992101e344e81da6"

#Initialize the speech recognition and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speech(text):
    """
    Conver text to speech."""
    engine.say(text)
    engine.runAndWait()

def recognize_speech_from_mic():
    """
    Handles speech recognition from a microphone input.
    Keeps asking for input until successful.
    """
    global recognizer
    global microphone  
    
    # Infinite Loop for Continuous Recognition:
    while True:
            try:
                with sr.Microphone() as source:
                    # Recognize speech from microphone with a timeout and phrase limit
                    audio = recognizer.listen(source, timeout=2, phrase_time_limit=2)
                    text = recognizer.recognize_google(audio)
                    # speech(f"You said: {text}")
                    print(text) 
                    return text
                
            # Handle errors during speech recognition    
            except sr.UnknownValueError:
                #Sorry, I did not understand that.
                speech("Please try again.")
         
            except sr.RequestError:
                #Sorry, there was an error with the speech recognition service.
                speech("Please try again.")
                
            except sr.WaitTimeoutError:
                #Listening timed out while waiting for phrase to start.
                speech("Please try again.")

def website(name):
    """Get the URL for a given song from the music library"""
    url = musicLibrary.get(name)
    return url

def news(news_api_key):
    """Fetch and announce the top news headlines"""
    # Make an HTTP GET request to the news API
    news = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={news_api_key}")
    if news.status_code == 200:
        # Parse the JSON response
        data = news.json()
        # Extract articles from the response
        articles = data.get("articles", [])
        # Announce each article's title
        for article in articles:
            title = article.get("title")
            speech(f"Title: {title}")
        else:
            speech(f"Failed to retrieve news. Status code: {news.status_code}")

def placetrade():
    """Automate the process of placing a trade on Trading view."""
    # Pause and wait for trading view to start 
    time.sleep(5)
    g = "Sir, do you want to buy or sell"
    speech(g)
    c = recognize_speech_from_mic()

    if "buy" in c.lower() or "kharido" in c.lower():
        # Automate 'buy' action in TradingView
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
        # Automate 'sell' action in TradingView
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


def recognize_command(c):
    """Recognize and execute commands based on speech input"""
    if "open" in c.lower():
        #For opening Websites. Add more according to your need
        if "open google" in c.lower():
            speech("Opening Google")
            wb.open("https://www.google.co.in/")
        elif "open facebook" in c.lower():
            speech("Opening Google")
            wb.open("https://www.facebook.com/")
        elif "open youtube" in c.lower():
            speech("Opening YouTube")
            wb.open("https://www.youtube.com/")

        #For opening applitcations. Add more Applications according to your need and use positonfinder.py to get the x,y cordinates of your UWP Applications. For other applications use the subprocess.run method and provide the file path
        elif "file explorer" in c.lower(): #Working
            speech("Opening File Explorer")
            if sys.platform == 'win32':
                subprocess.run(['explorer.exe'])
            elif sys.platform == 'darwin':
                subprocess.run(['open', '-a', 'Safari']) #Choose platform appropriate command
            elif sys.platform == 'linux':
                subprocess.run(['firefox']) #Choose platform appropriate command
            else:
                print("Unsupported platform")

        elif "whatsapp" in c.lower(): #Working
            speech("Opening whatsapp")
            pyautogui.click(x=731,y=738)

        elif "edge" in c.lower(): #Working
            speech("Opening Microsoft edge")
            if sys.platform == 'win32':
                subprocess.run([r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"])
            elif sys.platform == 'darwin':
                subprocess.run(['open', '-a', 'Safari'])#Choose platform appropriate command
            elif sys.platform == 'linux':
                subprocess.run(['firefox'])#Choose platform appropriate command
            else:
                print("Unsupported platform")

        elif "trading view" in c.lower() or "tradingview" in c.lower() or "trading" in c.lower():
            speech("Opening Trading view")
            pyautogui.click(x=722,y=738)
            speech("Sir, do  you want to place a trade")
            c = recognize_speech_from_mic()
            if "yes" in c.lower() or "theek" in c.lower() or "thik" in c.lower() or "place a trade" in c.lower() or "okay" in c.lower():
                placetrade()

        #For opening emails.
        elif "outlook" in c.lower() or "emails" in c.lower():
            speech("Opening Outlook")
            pyautogui.click(x=864,y=741)

    #For playing music. Add more songs to the musicLibrary according to your need    
    elif "play" in c.lower():
        try:
            command = c.split(" ")
            song = str(command[1]).lower()
            if song in musicLibrary:
                speech(f"Playing {song}")
                wb.open(website(song))
        except Exception as e:
            print(e)

    #Show news based on command        
    elif "news" in c.lower():
        news(news_api_key)
    
    #Handle invalid commands
    else:
        speech("Please provide a valid command")