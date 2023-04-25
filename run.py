from PyQt5 import QtWidgets, QtGui,QtCore
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import pyttsx3
import speech_recognition as sr
import os
import time
import webbrowser
import wikipedia 
import datetime
import requests
from bs4 import BeautifulSoup
import pywhatkit as kit
import pyjokes


flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("hello boss good morning.....i hope you are having a great day how can i help you")
    elif hour>=12 and hour<17:
        speak("hello boss good afternoon........ i hope you are having a great day how can i help you")
    elif hour>=17 and hour<21:
        speak("hello boss good evening......... i hope you are having a great day how can i help you")
    else:
        speak("hello boss i hope you are having a good day how can i help you")


class mainT(QThread):
    def __init__(self):
        super(mainT,self).__init__()
    
    def run(self):
        self.JARVIS()
    
    def STT(self):
        R = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listning...........")
            audio = R.listen(source)
        try:
            print("Recog......")
            text = R.recognize_google(audio,language='en-in')
            print(">> ",text)
        except Exception:
            print("Sorry Speak Again")
            return "None"
        text = text.lower()
        return text

    def JARVIS(self):
        
        while True:
            query = self.STT()
            if "activate" in query or "hi jarvis" in query:
                print(wish())
                speak(wish())
                
                query = self.STT()
                if "search" in query or "google" in query or "find" in query:
                    speak("searching details.. please wait")
                    query = query.replace("webbrowser"," ")
                    result=webbrowser.open(query)
                    print(result)
                    speak(result)

                elif "temperature" in query:
                    place = query.replace("temperature in","")
                    search = f"temperature in {place}"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div",class_="BNeawe").text
                    speak(f"current {search} is {temp}")

                elif "weather" in query:  
                    place1 = query.replace("weather in"," ")
                    api_address = "http://api.openweathermap.org/data/2.5/weather?appid=163bf245abaadd37b7e47e11389d0643&q="
                    weather_url = api_address+place1
                    json_data = requests.get(weather_url).json()
                    weather_rep = json_data['weather'][0]['description']
                    speak("weather is")
                    speak(weather_rep)

                    
                elif "who are you" in query:
                    speak("hi my name is jarvis, I'am a voice command assistant made by shubham tripathi")

                
                elif "calculate" in query:
                    speak("please wait let me check")
                    query = query.replace("webbrowser","")
                    result=webbrowser.open(query)
                    print(result)
                    speak(result)
                   
        
                elif "where is" in query or "find location for" in query:
                    query = query.replace("where is"," ")
                    location = query
                    speak("findind details for")
                    speak(location)
                    webbrowser.open("https://www.google.nl/maps/place/"+ location +"")   

            
                elif "joke" in query:
                    print(pyjokes.get_joke())
                    speak(pyjokes.get_joke())

                elif "corona" in query or "covid" in query or "kovid" in query or "korona" in query:
                    print(query)
                    speak("serching details please wait")
                    webbrowser.open("https://www.mohfw.gov.in/")

                elif "vaccination" in query or "vaccine" in query:
                    speak("searching details please wait")
                    webbrowser.open("https://www.cowin.gov.in/home")    
         
                elif "wikipedia" in query:
                    speak("searching details.. please wait")
                    query = query.replace("wikipedia"," ")
                    result = wikipedia.summary(query)
                    speak(result)
                    
        

                elif "play" in query:
                    query = query.replace("play"," ")
                    kit.playonyt(query)
                    speak("wait a second")       
        
                elif "open google" in query:
                    webbrowser.open("www.google.co.in")
                    speak("opening google")

                elif "open youtube" in query:
                    webbrowser.open("www.youtube.com")
                    speak("opening youtube")

                elif "open mail" in query:
                    webbrowser.open("https://www.google.com/gmail")
                    speak("opening gmail")        
            
                elif "goodbye" in query or "bye" in query:
                    speak("good bye boss, ")
                    exit()
                else:
                    speak("i don't understand what you are saying")
        
            else:
                speak("invalid activation command")
                print("invalid activation command")
                           





 
 
 
FROM_MAIN,_ = loadUiType(os.path.join(os.path.dirname(__file__),"./scifi.ui"))

class Main(QMainWindow,FROM_MAIN):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(1920,1080)
        self.label_7 = QLabel
        self.exit.setStyleSheet("background-color: rgb(255, 32, 3);\n"
        "border:none;")
        self.exit.clicked.connect(self.close)
        self.setWindowFlags(flags)

        Dspeak = mainT()
        self.label_7 = QLabel
        self.background.setStyleSheet("background-color: rgb(0, 0, 0);\n")
        
        
        self.ts = time.strftime("%A, %d %B")
        self.tm = time.strftime("%H: %M")
        
        Dspeak.start()
        
        self.label_5.setText("<font size=8 color='red'>"+self.ts+"</font>")
        self.label_5.setFont(QFont(QFont('Acens',14)))
        self.label_3.setText("<font size=8 color='white'>"+self.tm+"</font>")
        self.label_3.setFont(QFont(QFont('Acens',14)))


app = QtWidgets.QApplication(sys.argv)
main = Main()
main.show()
app.exec_()
exit()