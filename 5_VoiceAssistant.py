import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time

def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio=recognizer.listen(source)
        try:
            print("recognizing...")
            data=recognizer.recognize_google(audio)
            return data
        
        except sr.UnknownValueError:
            print("Not Understanding")


def speechtx(x):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    rate=engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':
    
    if "hey peter" in sptext().lower():
        while True:
            data1= sptext().lower()
            
            if "your name" in data1:
                name="my name is durjoy"
                speechtx(name)
                
            elif "old are you" in data1:
                age="I'm twenty years old."
                speechtx(age)
                
            elif 'time' in data1:
                time=datetime.datetime.now().strftime("%I%M%p")
                speechtx(time)
            
            elif 'youtube' in data1:
                webbrowser.open("https://www.youtube.com/")
            elif 'facebook' in data1:
                webbrowser.open("https://web.facebook.com/")
            
            elif "joke" in data1:
                joke_1=pyjokes.get_joke(language="en",category="neutral")
                print(joke_1)
                speechtx(joke_1)
            
            # elif "play movie " in data1:
            #     add="D:\Movie"
            #     list_movie=os.listdir(add)
            #     print(list_movie)
            #     os.startfile(os.path.join(add,list_movie[0]))
            
            elif "play music" in data1:
                add="D:\Music"
                list_music=os.listdir(add)
                print(list_music)
                os.startfile(os.path.join(add,list_music[0]))
            
            elif "exit" in data1:
                speechtx("thank you")
                break
            time.sleep(10)
            
    else:
         print("Thanks")