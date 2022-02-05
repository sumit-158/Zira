import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime

start = pyttsx3.init("sapi5")
voices = start.getProperty("voices")
start.setProperty("voice", voices[1].id)

def speak(auido):
    start.say(auido)
    start.runAndWait()

def welcome():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")
    elif hour>=12 and hour<17:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("Hey there, I'm zira! how can i help you?")
    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') 
        print(f"User said: {query}\n")  
    except Exception as e:
        print("Say that again please...")   
    return query
 
if __name__=="__main__" :
    welcome()
    while True:
        query = takeCommand().lower() 
        if 'wikipedia' in query:  
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
 