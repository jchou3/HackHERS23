import time
from flask import Flask, render_template, request, redirect
from pynput import mouse
from pynput import keyboard
from pynput.keyboard import Key, Listener
from threading import Thread
from time import sleep
import speech_recognition as sr
import pyttsx3
import sqlite3

synthesizer = pyttsx3.init()

rate = synthesizer.getProperty('rate')
synthesizer.setProperty('rate', 160)

app = Flask(__name__)
r = sr.Recognizer()

synthesizer.say("Welcome. Please press the space bar to begin request.") 
synthesizer.runAndWait() 
time.sleep(1)
synthesizer.say("To read a summary, Say read news or read research followed by article name and topic") 
synthesizer.runAndWait()
time.sleep(1) 
synthesizer.say("To search for articles, say search news or research, followed by topic") 
synthesizer.runAndWait() 
synthesizer.stop()

def on_press(key):
    print("Key noticed")
    check_key(key)
    with sr.Microphone() as source:
        # read the audio data from the default microphone
        #print("Speak now, please.")
        try:
                audio_data = r.record(source, duration=6)
                print("Recognizing...")
                # convert speech to text
                text = r.recognize_google(audio_data)
                print(text)
                if ("read" not in text):
                    synthesizer.say("Unable to recognized article. Please hold the space bar and say “read” followed by the article’s name you want to summarize.") 
                    synthesizer.runAndWait() 
                    synthesizer.stop()
                else:
                    decipher(text)
                    return
        except:
                print("An exception occurred")               
 
def decipher(text):
    synthesizer.say("poopoopeepee")
    synthesizer.runAndWait() 
    synthesizer.stop()
    try:
            print("Recognizing...")
            audio_data = r.record(source, duration=6)
            #convert speech to text
            text = r.recognize_google(audio_data)
            print(text)
            if ("read" in text):

                return
            elif ("search" in text):
                
                return
            else:
                synthesizer.say("Unable to find article. Please try again") 
                synthesizer.runAndWait() 
                synthesizer.stop()
                
    except:
            print("An exception occurred")

def on_release(key):
    #print('{0} release'.for8mat(
       # key))
    # if key == Key.esc:
         # Stop listener
    print("released")
    return True

def check_key(key):
    if key == keyboard.Key.space: 
        print("Space pressed")

def keyboardListener():
    print("Help")
    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
    listener.start()

@app.route("/")
def home():
    thr = Thread(target=keyboardListener, args=[])
    thr.start() 
    #below is my query stuff 
    connection = sqlite3.connect("databases/data.db")
    crsr = connection.cursor()
    query = "SELECT * FROM News WHERE"
    crsr.execute(query)
    res = crsr.fetchall()
    for i in res:
        print(i[2])
    connection.commit()
    connection.close()
    return render_template("view.html", res=res)
    #return render_template("view.html")
    return render_template("view.html")



if __name__ == "__main__":
    app.run(debug=True, port=8000)



