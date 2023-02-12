import time
from flask import Flask, render_template, request, redirect
from pynput import mouse
from pynput import keyboard
from pynput.keyboard import Key, Listener
from threading import Thread
from time import sleep
import speech_recognition as sr
import pyttsx3

synthesizer = pyttsx3.init()

rate = synthesizer.getProperty('rate')
synthesizer.setProperty('rate', 175)

app = Flask(__name__)
r = sr.Recognizer()

def intro():
    synthesizer.say("Hello, Welcome. Please press the space bar and say read news or read research followed by the article name you want to summarize and its topic.") 
    synthesizer.runAndWait() 
    synthesizer.stop()

def on_press(key):

    print("Key noticed")
    check_key(key)
    while (True):
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
    intro
    thr = Thread(target=keyboardListener, args=[])
    thr.start() 
    synthesizer.say("poopoopeepee")
    synthesizer.runAndWait() 
    synthesizer.stop()
       
    return render_template("view.html")

if __name__ == "__main__":
    app.run(debug=True, port=8000)

def query(keyWords):
    return 1
