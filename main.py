import speech_recognition as sr
import pyttsx3 
import modules

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speech(text):
    engine.say(text)
    engine.runAndWait()
    
if __name__ == "__main__":
    speech("Initialzing Jarvis....")
    while True:
        # recognize speech using google
        try:
            # obtain audio from the microphone
            with sr.Microphone() as source:
                print("Say something!")
                audio = recognizer.listen(source, timeout=2,phrase_time_limit=2)
            activate_command = recognizer.recognize_google(audio)
            if(str(activate_command).lower().__contains__("jarvis")):
                speech("Hlo Sir, How may I Help You")
                with sr.Microphone() as source:
                    print("Jarvis Active")
                    audio = recognizer.listen(source, timeout=2, phrase_time_limit=2)
                    command = recognizer.recognize_google(audio)
                    # speech(command)
                    modules.recognize_command(command)
                    print(command)
            elif "stop" in activate_command:
                        break
        except sr.UnknownValueError:
            print("Jarvis could not understand audio")
        except sr.RequestError as e:
            print("Jarvis error; {0}".format(e))