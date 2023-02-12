import time
from flask import Flask, render_template, request, redirect
from pynput import mouse
from pynput import keyboard
from pynput.keyboard import Key, Listener
from threading import Thread
from time import sleep
import speech_recognition as sr
import pyttsx3
import pdftotxt as ptt
from bs4 import BeautifulSoup as s
import requests
import os
from werkzeug.utils import secure_filename


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
            print("Recognizing...")
            audio_data = r.record(source, duration=6)
            # convert speech to text
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
        return render_template("view.html")

@app.route("/upload_file", methods = ['GET'])
def upload_file():
    print("hello")
    #file = request.files('filename')
    # file_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename))
    # f = request.files['file']
    # f.save(file_path)
    # print(file)
    # print(os.path.exists(file))
    selectedFile = view.getElementById('file').files[0]
    ptt.read_and_interpret_pdf(selectedFile)
    return render_template("view.html")

if __name__ == "__main__":
    app.run(debug=True, port=8000)

def query(keyWords):
    return 1
