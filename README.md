# Jarvis - Personal Voice Assistant

Jarvis is a personal voice assistant designed to perform various tasks based on voice commands. It can play music, fetch news, open applications, and interact with different web services. This project combines speech recognition, text-to-speech, and GUI automation to create a versatile and interactive assistant, and can generate automatic responses via OpenAI for things it doesn't know.

## Project Structure
1. main.py: The main entry point of the application. It listens for voice commands and interacts with the user.
2. modules.py: Contains functions for handling specific tasks like playing music, fetching news, generating automatic respones and opening applications.
   
## Installation

To get started with Jarvis, clone the repository and install the required libraries using pip.
```
$ git clone https://github.com/your-username/jarvis.git
$ cd jarvis
$ pip install -r requirements.txt
```

**Requirements:**

**1. speech_recognition**

**2. pyttsx3**

**3. requests**

**4. pyautogui**

**5. pyperclip**

**6. subprocess**

**7. openai**
   
## Usage

### Running Jarvis

To start the Jarvis assistant, run the following command:

`python main.py`

Jarvis will greet you and wait for commands. You can say "Jarvis" followed by your command. For example:
1. **"Jarvis, play soch":** Plays the song "Soch".
2. **"Jarvis, fetch news":** Fetches and reads out the latest news headlines.
   
### 'main.py' Overview

The **'main.py**' file is responsible for:
1. Initializing the speech recognizer and text-to-speech engine.
2. Listening for activation commands and processing user commands.
3. Handling errors related to speech recognition.
   
**_Key Functions_**
1. **speech(text)**: Converts text to speech using pyttsx3.
2. **recognize_speech_from_mic()**: Captures and recognizes speech from the microphone.
3. **recognize_command(command)**: Processes the given command and triggers corresponding actions.
   
### 'modules.py' Overview

The modules.py file contains functions to handle various tasks based on voice commands.

_**Key Function**_
1. **speech(text)**: Converts text to speech.
2. **recognize_speech_from_mic()**: Recognizes speech from the microphone and returns the recognized text.
3. **website(name)**: Returns the URL for a given song from the musicLibrary.
4. **news(api_key**): Fetches and announces the latest news headlines using the provided API key.
5. **placetrade()**: Automates placing a trade on TradingView based on user input.
6. **autoresponse(c)**: Generates automatic response via OpenAI.
7. **recognize_command(c)**: Processes and executes commands such as opening websites, applications, and playing music.

## Customization

### Adding New Songs

To add new songs to the music library, update the musicLibrary dictionary in modules.py with new entries.

`
musicLibrary = {
    "song_name": "https://www.youtube.com/watch?v=your_video_id"
} `

### Modifying Commands

To modify or add new commands, update the recognize_command(c) function in modules.py. For example, to add a new application:
```
elif "application_name" in c.lower():
    speech("Opening Application Name")
    # Add code to open the application
```
 
### Configuring API Key

To configure the news API key, replace the placeholder in modules.py:

` news_api_key = "your_api_key" `

To configure the openai API key, replace the placeholder in modules.py:

` opneai_api_key = "your_api_key" `

### Adding New Applications

To open new applications, update the recognize_command(c) function with the appropriate commands for your operating system:
```
elif "application_name" in c.lower():
    speech("Opening Application Name")
    if sys.platform == 'win32':
        subprocess.run(['path_to_application'])
    elif sys.platform == 'darwin':
        subprocess.run(['open', '-a', 'Application Name'])
    elif sys.platform == 'linux':
        subprocess.run(['application_command'])
    else:
        print("Unsupported platform")
```
    
## Troubleshooting
1. Speech Recognition Issues: Ensure your microphone is properly set up and permissions are granted.
2. Application Not Opening: Verify the file paths and commands for the applications you wish to open.

## Contributing
Contributions are welcome! If you have suggestions or improvements, please fork the repository and create a pull request.

