import pyttsx3
import datetime
import speech_recognition as sr
import sys
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You:{query}\n")

    except Exception as e:
        print(e)
        print("Sorry, please say that again or verify....")
        return "None"
    
    return query 

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(day)
    speak(month)
    speak(year)
    
def wishme():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good Morning Ron")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Ron")
    elif hour >= 18 and hour < 22:
        speak("Good Evening Ron") 
    else:
        speak("Welcome Back Ron")
    speak("Friday at your service")
    speak("How may I help you?")

def wiki(q):
    speak("Searching...")
    q = q.replace("wikipedia","")
    result = wikipedia.summary(q, sentences = 2)
    print(result)
    speak(result)

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(user, password)
    server.sendmail(user, to, content)
    server.close()

def Email():
    try:
        speak("What do you want to send, Ron?")
        content = takeCommand()
        to = '<insert recipient email>'
        sendEmail(to, content)
        speak("Email has been sent!")
    except Exception as e:
        print(e)
        speak("Unable to send email")

def chrome():
    speak("What should I search?")
    chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    search = takeCommand().lower()
    wb.get(chromepath).open_new_tab(search)

def remember():
    speak('Do you want me to take a note?')
    yn = takeCommand()
    if 'yes' in yn:
        speak('Yes Ron, What should I make note of?')
        data = takeCommand()
        speak('Repeating what you just said for clarification' + data)
        note = open('data.txt', 'w')
        note.write(data)
        note.close()
    elif 'no' in yn:
        speak('So do you want me to tell you')
        speak('the notes you asked me to take')
        dec = takeCommand()
        if 'yes' in dec:
            note = open('data.txt', 'r')
            speak('Sure sir, The notes you asked me to make are' + note.read())
        elif 'no' in dec:
            speak('Okay')
    else:
        speak('Could not get you Ron')

def screenshot():
    img = pyautogui.screenshot()
    img.save('C:\\Users\\Ron\\Projects\\Python\\JARVIS\\ss.png')
    speak("Done!")

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU usage is at" + usage)
    battery = psutil.sensors_battery()
    speak("Current Battery state is at")
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())

def quit():
    speak("Bella Ciao Ron!")
    sys.exit()

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if "time" in query:
            time()

        elif "date" in query:
            date()

        elif "wikipedia" in query:
            wiki(query)

        elif 'send email' in query:
            Email()

        elif "chrome" in query:
            chrome()

        elif 'make note' in query or 'remember' in query or 'know' in query:
            remember()

        elif 'usage' in query or 'cpu' in query:
            cpu()

        elif 'joke' in query:
            jokes()

        elif 'logout' in query:
            os.system('shutdown -l')

        elif 'shutdown' in query:
            os.system('shutdown /s /t 1')

        elif 'restart' in query:
            os.system('shutdown /r /t 1') 

        elif 'screenshot' in query:
            screenshot()

        elif "goodbye" in query:
            quit()