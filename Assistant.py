from sys import implementation
import pyttsx3
import pyaudio
import datetime
import wikipedia
import webbrowser
import speech_recognition as sr
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=4 and hour <=11:
        speak("Good Morning!")
    elif hour>=12 and hour<=16:
        speak("Good afternoon!")
    elif hour>=17 and hour<=20:
        speak("Good Evening!")
    else:
        speak("Good Night!")
    speak("I am Josef. please tell me how may I help you.")   


def takeCommand():
    # It takes microphone input from user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold = 1
        audio=r.listen(source)
    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        # print(e)
        print("say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("codecodingexam@gmail.com", 'passwd set this ')
    server.sendmail("codecodingexam@gmail.com", to, content)
    server.close()




if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()
        # Logic for executing task based on query
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentence=2)
            speak("According tro wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'open aljazeera' in query:
            webbrowser.open("aljazeera.com")
        elif 'open thehindu' in query:
            webbrowser.open("thehindu.com")   
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'open code' in query:
            codePath = "C:\\Users\\darul Haram\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startFile(codePath)
        elif 'email to Aamir' in query:
            try:
                speak("whas should I say")
                content = takeCommand()
                to = "codecodingexam@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")

            except Exception as e:
                    print (e)
                    speak("Sorry my friend Ammir. I am not able to send this email")

        elif 'quit' in query:
                 exit()





        
    
 

