import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wd
import os
import pyautogui
import psutil
import pyjokes


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


def sendEmail(to,content):
    server=smtplib.SMTP('smtp.com',587)
    server.ehlo()
    server.starttls()
    server.login('abcd@gmail.com','123')
    server.sendmail('abcd@gmail.com', to,content)
def serachInChrome(search):
    chromepath='C:/Program Files (x86)\Google/Chrome/Application/chrome.exe %s'
    wd.get(chromepath).open_new_tab(search + '.com')
    print('open')
    
            
def SystemControl():
    speak('What You Want To Do sir?')
    takeQury=takeCommand().lower()
    if 'logout' in takeQury:
         os.system('shutdown -s')
    elif 'shutdown' in takeQury:
        os.system('shutdown /s /t 1')
    elif 'restart' in takeQury:
        os.system('shutdown /s /t 1')
    else:
        speak("Don't Understand Sir")
        return
def screenshot():
    img=pyautogui.screenshot()
    img.save("D:\\study\\python\\Jarvis\\img\\ss.png")
    return

def PlaySong():
    song_dir='D:\\Music'
    songs=os.listdir(song_dir)
    os.startfile(os.path.join(song_dir,songs[0]))


def addRememberThat(data):
    remember=open('data.txt','w')
    remember.write(data)
    remember.close()
    return
def rememberThat():
    remember=remember.open()
    speak("wait a Sec Sir")
    speak("This ios what you want me to remeber")
    speak(remember.read())
    return
def systemStatus():
    usage=str(psutil.cpu_percent())
    speak("CPU is at "+usage)
    battery=psutil.sensors_battery()
    speak('Battery Is at'+battery.percent)
def tellAJoke():
    speak(pyjokes.get_joke())
    return

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
        elif 'send email' in query :
            try:
                speak('what should i sent?')
                content=takeCommand()
                speak('Whom Should i Send?')
                to=takeCommand()
                sendEmail(to,content)
        elif 'search in chrome' in query:
            speak("What Should You i search ?")
            search=takeCommand().lower()
            serachInChrome(search)
        elif 'system commands' in query:
            SystemControl()
        elif 'play songs' in query:
            PlaySong()
        elif 'remember that' in query:
            speak("What Should I remebr? Sir")
            data=takeCommand()
            speak("You Said me to remember that"+data)
            addRememberThat(data)
        elif 'do i have anythig to remember?' in query:
            rememberThat()
        elif 'take screenshot' in query:
            screenshot()
            speak("Done")
        elif 'system status' in query:
            systemStatus()
        elif 'tell me a joke' in query:
            tellAJoke()

            
            


            
        elif 'offline' in query:
            quit()
        
