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
import sqlite3
from werkzeug.utils import secure_filename


synthesizer = pyttsx3.init()


rate = synthesizer.getProperty('rate')
synthesizer.setProperty('rate', 160)

app = Flask(__name__)
r = sr.Recognizer()

def getSummary(type, title):

    if type != "news" and type != "research":
        return None
    
    connection = sqlite3.connect("databases/data.db")
    cur = connection.cursor()
    if type == "news":
        cur.execute("SELECT * FROM News")
    else:
        cur.execute("SELECT * FROM Research")
    data = cur.fetchall()

    match = ""

    for word in title:
        match += word
        match += " "

    for item in data:
        if match in item[1].lower():
            return item[3]


    return None


def getTopics(type, topic):
    print("in method")

    if type != "news" and type != "research":
        return None

    connection = sqlite3.connect("databases/data.db")
    cur = connection.cursor()
    if type == "news":
        cur.execute("SELECT * FROM News")
    else:
        cur.execute("SELECT * FROM Research")
    data = cur.fetchall()

    titles = []

    for item in data:
        if topic in item[2].lower():
            titles.append(item[1])

    return titles

def find_words_after_read(s):
    words = s.split()
    for i, word in enumerate(words):
        if word == "read":
            try:
                type = words[1]
                title = words[2:]
                return type, title
            except IndexError:
                return None, None, None
    return None, None, None

def find_words_after_search(s):
    words = s.split()
    for i, word in enumerate(words):
        if word == "search":
            try:
                next_word = words[i + 1]
                last_word = words[-1]
                print(next_word)
                print(last_word)
                return next_word, last_word
            except IndexError:
                return None, None
    return None, None

def on_press(key):

    if key == keyboard.Key.shift:
        with sr.Microphone() as source:
            # read the audio data from the default microphone
            #print("Speak now, please.")
                print("Recognizing...")
                audio_data = r.record(source, duration=10)
                # convert speech to text
                text = r.recognize_google(audio_data)
                print(text)
                text = text.lower()
                
                if ("read" in text):
                    type, article_name = find_words_after_read(text)
                    sum = getSummary(type, article_name)

                    #return none if can't find.
                    if sum:
                        words = sum
                    else:
                        words = "Article not found. Please try again."
                        
                elif ("search" in text):
                    type , topic = find_words_after_search(text)
                    articles = getTopics(type, topic)

                    if articles:
                        words = "There are " + str(len(articles)) + " articles under " + topic + ". "
                        for name in articles:
                            words += name
                            words += ", "
                        print(words)
                    else:
                        words = "No articles found under " + topic + ". Please try again."

                else:
                    words = "Unable to understand. Please try again."
                synthesizer.say(words)
                synthesizer.runAndWait() 
                synthesizer.stop()
                    
    elif key == keyboard.Key.left:
        synthesizer.say("Welcome. Please press shift to begin request. To read a summary, say read news or read research, followed by article name. To search for articles, say search news or search research, followed by topic. To repeat these instructions, press the left arrow key.") 
        synthesizer.runAndWait() 
        synthesizer.stop()

    return True
    
                
def on_release(key):
    #print('{0} release'.for8mat(
       # key))
    # if key == Key.esc:
         # Stop listener
    return True


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
    connection = sqlite3.connect("databases/data.db")
    cur = connection.cursor()
    cur.execute("SELECT * FROM News")
    data = cur.fetchall()
    return render_template("view.html", data = data)

@app.route("/upload_file", methods = ['GET'])
def upload_file():
    print("hello")
    #file = request.files('filename')
    # file_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename))
    # f = request.files['file']
    # f.save(file_path)
    # print(file)
    # print(os.path.exists(file))
    
    return render_template("view.html")

if __name__ == "__main__":
    app.run(debug=True, port=8000)



