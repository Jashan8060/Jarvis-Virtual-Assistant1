import webbrowser
import requests
import pyttsx3
import speech_recognition as sr
musicLibrary ={
    "soch": "https://www.youtube.com/watch?v=E8rpY2FwKkY&pp=ygUEc29jaA%3D%3D",
    "perfect": "https://www.youtube.com/watch?v=2Vv-BfVoq4g&pp=ygUHcGVyZmVjdA%3D%3D",
    "friends": "https://www.youtube.com/watch?v=jzD_yyEcp0M&pp=ygUNZW5nbGlzaCBzb25ncw%3D%3D",
    "runaway":"https://www.youtube.com/watch?v=d_HlPboLRL8&pp=ygUGYXVyb3Jh"
}
api_key = "faa878d35a854d73992101e344e81da6"

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speech(text):
    engine.say(text)
    engine.runAndWait()

def website(name):
    url = musicLibrary.get(name)
    return url

def news(api_key):
    news = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}")
    if news.status_code == 200:
    # Parse the JSON response
        data = news.json()
    
        # Extract articles from the response
        articles = data.get("articles", [])
        
        # Print each article's title
        for article in articles:
            title = article.get("title")
            speech(f"Title: {title}")
        else:
            speech(f"Failed to retrieve news. Status code: {news.status_code}")

def recognize_command(c):
    if "open" in c.lower():
        if "open google" in c.lower():
            speech("Opening Google")
            webbrowser.open("https://www.google.co.in/")
        elif "open facebook" in c.lower():
            speech("Opening Google")
            webbrowser.open("https://www.facebook.com/")
        elif "open youtube" in c.lower():
            speech("Opening YouTube")
            webbrowser.open("https://www.youtube.com/")
    elif "play" in c.lower():
        command = c.split(" ")
        song = str(command[1]).lower()
        if song in musicLibrary:
            speech(f"Playing {song}")
            webbrowser.open(website(song))
    elif "news" in c.lower():
        news(api_key)