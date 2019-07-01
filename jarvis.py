import pyttsx3
import speech_recognition as sr 
import wikipedia
import webbrowser
import datetime
import os
import smtplib
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour <12:
        speak("Good Morning Master")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Master")

    elif hour >=18 and hour < 20:
        speak("Good Evening Master")

    else:
        speak("Good Night Master")

    speak("I am Jarvis Sir.Speed 1 terahertz, memory 1 zeta byte. Please tell me how may I help you")

def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again Please....")
        return "None"
    return query


def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('akashtawade2693@gmail.com','akash1493')
    server.sendmail('akashtawade2693@gmail.com',to,content)
    server.close()

if __name__ == "__main__":
    #speak("Akash is a good boy")
    wishMe()

    while True:
        query = takeCommand().lower()

        # Logic for executing task based on query
        if 'wikipedia'in query:
           speak('Searching Wikipedia.....')
           query = query.replace("wikipedia","")
           results = wikipedia.summary(query, sentences=5)
           speak("Accoreding to wikipedia")
           print(results)
           speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'open gmail' in query:
            webbrowser.open("gmail.com")

        elif 'play music' in query:
            music_dir = 'D:\\C Drive\\Music\\My_Fav_Songs'
            songs = os.listdir(music_dir)
            print(songs)
            value = random.randint(0,4)
            os.startfile(os.path.join(music_dir,songs[value]))

        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")

        
        elif 'open visual studio code' in query:
            codePath = 'D:\\CDAC Project\\Microsoft VS Code\\Code.exe'
            os.startfile(codePath)

        elif 'email to akash' in query:
            try:
                speak("what should I say")
                content = takeCommand()
                to = "akashtawade2693@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry sir....I am not able to send this Email")