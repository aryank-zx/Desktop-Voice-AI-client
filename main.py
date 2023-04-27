import pyttsx3
import datetime
import os
import smtplib
import sys
import wikipedia
import webbrowser
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

wikipedia.set_lang("simple")
sys.stdout.reconfigure(encoding='utf-8')

def wishme():
 hr = int (datetime.datetime.now().hour)
 speak("Hello Aryan sir, how can I help you")

def speak(audio):
 engine.say(audio) 
 engine.runAndWait() 

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('aryankarkra@gmail.com', 'lgpyhnxkitvmzziz')
    server.sendmail('aryankarkra@gmail.com', to, content)
    server.close()

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
        return "None" 
    return query
 
if __name__ == "__main__":
    wishme()
    while True:
    # if 1:
        query = takeCommand().lower() #Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            # print(results.encode('utf-8').decode(sys.stdout.encoding))
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:
            music_dir = 'C:/Users/aryan/Music/My_Songs'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        
        elif 'open code' in query:
            codePath = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Sublime Text 3.lnk"
            os.startfile(codePath)
        
        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "aryankarkra@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
                print("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Error detected")    