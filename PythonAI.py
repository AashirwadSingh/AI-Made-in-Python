import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import datetime

engine = pyttsx3.init()
engine.setProperty('rate', 155)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:

        print("Listening...\n")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...\n")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")

    except Exception as e:

        print("Sorry, Not able to listen.")
        speak("Sorry, Not able to listen.")
        return "None"

    return query

def wishMe():

    wishing_time = int(datetime.datetime.now().hour)
    print(wishing_time)

    if wishing_time >= 0 and wishing_time < 12:
        speak("Good Morning Sir!")

    elif wishing_time >= 12 and wishing_time < 15:
        speak("Good Afternoon Sir!")

    else:
        speak("Good Evening Sir!")

    speak("I am your Personal Assistant. How may I help You?")

if __name__ == "__main__":

    wishMe()

    while True:
        query = takeCommand().lower()

        if "wikipedia" in query or "search" in query:
            try:
                speak("Searching... Please Wait!")
                query = query.replace("wikipedia", "")
                query = query.replace("search", "")
                results = wikipedia.summary(query, sentences=3)
                print("According To Wikipedia...")
                speak("According to Wikipedia...")
                print(results)
                speak(results)

            except Exception as l:
                print(l)
                speak("Sorry Sir, No Results Found.")

        elif "open youtube" in query:
            speak("Opening Youtube...")
            webbrowser.open('https://www.youtube.com')
            speak("Opened Youtube!")

        elif "open google" in query:
            speak("Opening Google...")
            webbrowser.open('https://www.google.com')
            speak("Opened Google")

        elif "open gmail" in query:
            speak("Opening Gmail...")
            webbrowser.open('https://www.gmail.com')
            speak("Opened Gmail")

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"The Time is {strTime} Sir!")
        
        elif "bye" in query or "quit" in query:
            print("Bye Sir!")
            speak("Bye Sir Happy to help You.")
            exit()
