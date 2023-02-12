from flask import Flask, render_template, request, redirect
from pynput import mouse
from pynput import keyboard
from pynput.keyboard import Key, Listener
from threading import Thread
from time import sleep
import speech_recognition as sr

app = Flask(__name__)
r = sr.Recognizer()

def on_press(key):

    print("Key noticed")
    check_key(key)
    with sr.Microphone() as source:
        # read the audio data from the default microphone
        print("Speak now, please.")
        audio_data = r.record(source, duration=8)
        print("Recognizing...")
        # convert speech to text
        text = r.recognize_google(audio_data)
        print(text)

def on_release(key):
    #print('{0} release'.format(
       # key))
    # if key == Key.esc:
        # Stop listener
    print("released")


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

if __name__ == "__main__":
    app.run(debug=True, port=8000)
