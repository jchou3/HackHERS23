import pyttsx3
syn = pyttsx3.init()
voices = syn.getProperty('voices')
syn.setProperty('voice', voices[1].id)
my_text = input("Enter the text: ")
syn.say(my_text)
syn.runAndWait()
syn.stop()

