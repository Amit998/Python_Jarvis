import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia

engine=pyttsx3.init('dummy')


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)

def date():
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    date=int(datetime.datetime.now().day)
    speak(year)
    speak(month)
    speak(date)


def wishMe():
    speak("Wellcome Back Sir!")
    speak("Current Time Is")
    time()
    speak("The Current Date Is")
    date()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <18:
        speak("Good Morning Sir")
    elif hour >=12 and hour < 18:
        speak("Good After Noot Sir")
    elif hour >= 18 and hour<24 :
        speak("Good evening Sir")
    else:
        speak("Good Night Sir")

    speak("Jarvis at Your Service. Please tell me how can i help you?")


def takeCommand():
    r=sr.Recognizer()
    with  sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizating...")
        query=r.recognize_google(audio,language='en-in')
        print(query)
    except  Exception as e:
        print(e)
        # speak("Say That Again Please...")
        print("Cant Here You")

        return "None"
    return query

def wikiSearch(query):
    query=query.replace("wikipedia","")
    result = wikipedia.summary(query,sentences=2)
    print(result)
    speak(result)


# takeCommand()
# speak("hello")

if __name__ == "__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak('Searching...')
            wikiSearch(query)
            
        elif 'offline' in query:
            quit()
        
