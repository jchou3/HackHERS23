from flask import Flask, render_template, request, redirect
# from tkinter import Tk,Label
from pynput import mouse
from pynput import keyboard
from pynput.keyboard import Key, Listener
from threading import Thread
from time import sleep

app = Flask(__name__)

def on_press(key):
    #print('{0} pressed'.format(
        #key))
    print("Key noticed")
    check_key(key)

def on_release(key):
    #print('{0} release'.format(
       # key))
    # if key == Key.esc:
        # Stop listener
        print("released")
        return False

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
    # thr = Thread(target=keyboardListener, args=[])
    # thr.start()
    keyboardListener()
    return render_template("view.html")

if __name__ == "__main__":
    app.run(debug=True, port=8000)




# Collect events until released



