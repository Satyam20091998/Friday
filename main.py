import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty("rate",170)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir")

    elif hour>=12 and hour<18:
        speak("Good Afternoon  sir")

    else:
        speak("Good Evening sir")



def takeCommand():

    r = sr.Recognizer()
    microphone = sr.Microphone()
    with microphone as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('saty***@gmail.com', 'your-password')
    server.sendmail('**@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()


    while True:

        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:

            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        if ' who are you' in query:

            speak("I am Friday,Your Personal Assisstant!Friday, mean,Female Replacement Intelligent Digital Assistant Youth")

        elif 'hello friday' in query:
            speak("hello sir ,what i can do for you")



        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'repeat ' in query:
            speak("ok sir")
            while True:
                contant=takeCommand()
                speak(contant)
                if 'friday' in contant:
                    speak("im in your service")
                elif 'exit ' in contant:
                    break


        elif 'play music' in query:
            music_dir = 'D:\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[int(random.randrange(5))]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")


        elif 'email to satyam' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "*********@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email")
        elif 'quit' in query:
            speak("Okay sir,Thank you")
            exit()

#this is satyam markam
#this is the best thing when they call me