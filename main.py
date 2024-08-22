import speech_recognition as sr  # Import for speech recognition
import pyttsx3  # Import for text-to-speech conversion
import modules  # Import the custom module with various functions

# Initialize the speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speech(text):
    """Convert text to speech using pyttsx3."""
    engine.say(text)
    engine.runAndWait()
    
if __name__ == "__main__":
    # Greet the user and indicate that Jarvis is initializing
    speech("Initialzing Jarvis....")
    while True:
        # recognize speech using google
        try:
            # Recognize the speech command to activate Jarvis
            activate_command = modules.recognize_speech_from_mic()

            # Check if the command contains "Jarvis" to activate the assistant
            if(str(activate_command).lower().__contains__("jarvis")):
                speech("Hlo Sir, How may I Help You")
                print("Jarvis Activate")

                #Listen for the next command from the user
                command = modules.recognize_speech_from_mic()
                
                #Process the recognized command
                modules.recognize_command(command)

            # If the command is "stop", exit the loop and terminate the program
            elif "stop" in activate_command:
                        break
            
        except sr.UnknownValueError:
            # Handle cases where speech recognition fails to understand the audio
            print("Jarvis could not understand audio")

        except sr.RequestError as e:
            # Handle cases where there is an error with the speech recognition service
            print(f"Jarvis error; {e}")