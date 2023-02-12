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
import pdftotxt as ptt
#from bs4 import BeautifulSoup as s
import requests
import os
import sqlite3
from werkzeug.utils import secure_filename

import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf'}



synthesizer = pyttsx3.init()


rate = synthesizer.getProperty('rate')
synthesizer.setProperty('rate', 175)

app = Flask(__name__)
r = sr.Recognizer()


def find_words_after_read(s):
    words = s.split()
    for i, word in enumerate(words):
        if word == "read":
            try:
                next_word = words[i + 1]
                rest_of_words = words[i + 2:-1]
                last_word = words[-1]
                return next_word, rest_of_words, last_word
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
                return next_word, last_word
            except IndexError:
                return None, None
    return None, None

def on_press(key):
    if key == keyboard.Key.space:
        with sr.Microphone() as source:
            # read the audio data from the default microphone
            #print("Speak now, please.")
            try:
                print("Recognizing...")
                audio_data = r.record(source, duration=10)
                # convert speech to text
                text = r.recognize_google(audio_data)
                print(text)
                text = text.lower()
                
                if ("read" in text):
                    type, article_name, topic = find_words_after_read(text)
                    print(type)
                    print(article_name)
                    print(topic)
                elif ("search" in text):
                    type , topic = find_words_after_search(text)
                    print(type)
                    print(topic)
                else:
                    synthesizer.say("Unable to find article. Please try again") 
                    synthesizer.runAndWait() 
                    synthesizer.stop()
                    
            except:
                synthesizer.say("Unable to find article. Please try again") 
                synthesizer.runAndWait() 
                synthesizer.stop()
                
    elif key == keyboard.Key.shift:
        synthesizer.say("Welcome. Please press the space bar to begin request. To read a summary, say read news or read research, followed by article name. To search for articles, say search news or search research, followed by topic. To repeat these instructions, press the shift key.") 
        synthesizer.runAndWait() 
        synthesizer.stop()
    
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


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/upload_file", methods = ['GET', 'POST'])
def upload_file():
    print("ugh")
    if request.method == 'POST':
        print("posint")
        # check if the post request has the file part
        if 'file' not in request.files:
            print("*")
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            print("*")
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            print("*")
            filename = secure_filename(file.filename)
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(path)
            # return redirect(url_for('uploaded_file',
            #                         filename=filename))
            path = find_file(filename, "uploads")
            ptt.read_and_interpret_pdf(path[0])
            return redirect('http://127.0.0.1:8000')
        

        #print(file)
    return ''

from flask import send_from_directory

def find_file(filename, search_path):
   result = []

# Wlaking top-down from the root
   for root, dir, files in os.walk(search_path):
      if filename in files:
         result.append(os.path.join(root, filename))
   print(result)
   return result


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

if __name__ == "__main__":
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.secret_key = 'HACKHERS'

    app.run(debug=True, port=8000)



