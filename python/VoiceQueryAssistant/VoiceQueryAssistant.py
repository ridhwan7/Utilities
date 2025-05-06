import sys
import speech_recognition as sr
import pyttsx3
import webbrowser


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Register Brave browser
browser_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
webbrowser.register('brave', None, webbrowser.BackgroundBrowser(browser_path))

def speak(text):
    engine.say(text)
    engine.runAndWait()

def parse_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language='en-gb')
            print(f"You said: {query}")
            return query.lower()
        except sr.WaitTimeoutError:
            print("Listening timed out.")
        except sr.UnknownValueError:
            print("Sorry, I could not understand that.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
    return ""

def clean_query(query):
    # Remove unwanted characters
    blacklist = set("'+[]")
    return "".join(char if char not in blacklist else " " for char in query)

def main():
    speak("What would you like to know?")
    query = parse_command()
    if query:
        cleaned_query = clean_query(query)
        url = f"https://www.google.com/search?q={cleaned_query}"
        webbrowser.get('brave').open(url, new=2)
        speak(f"Here are the results for {cleaned_query}")
    else:
        speak("No query detected. Ending session.")

    print("Session Terminated")
    speak("Session Terminated")

if __name__ == '__main__':
    main()
