import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import os.path
import cv2
import random
import requests
import speedtest
from requests import get
import pywhatkit as kit
import smtplib
import sys
from bs4 import BeautifulSoup
import pyjokes
import pyautogui
import MyAlarm
import time
import operator
import requests, geocoder
import pytz
import instaloader
import PyPDF2
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from frontgui import Ui_BarbieWithBrain


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


#to wish
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Barbie  Mam. Please tell me how may I help you")
#to send email
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('','')
    server.sendmail('khardesonal18@gmail.com', to,content)
    server.close()

#for news updates
def news():
    main_url = "http://newsapi.org/v2/top-headlines?sources=techcrunch&apikey=5e60ce61d8f749c596c57147efc89f43"
    main_page = requests.get(main_url).json()
    #print main_page
    articles = main_page["articles"]
    #print(articles)
    head = []
    day =["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")

    
def pdf_reader():
    book=open('wu2010.pdf','rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speak(f"Total numbers of pages in this book{pages}")
    speak("mam please enter the page number i have to read")
    pg = int(input("Please enter the page number: "))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text)

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
    
    def run(self):
        speak("please say wakeup to continue")
        while True:
            self.query = self.takecommand()
            if "wake up" in self.query or "are you there" in self.query or "hello Barbie" in self.query:
                self.TaskExecution()


         #to convert voice to text
    def takecommand(self):      
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source, timeout = 4, phrase_time_limit = 7)

        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            speak("Say that again please.......")
            return "none"
        query = query.lower()
        return query
 
#if __name__ == "__main__":
        #takecommand()
    def TaskExecution(self):
        wish()
        while True:
        #if 1:

            self.query = self.takecommand().lower()
            #logic building for tasks

            if "open notepad" in self.query:
                npath = "C:\WINDOWS\system32\\notepad.exe"
                os.startfile(npath)
            elif "open command prompt" in self.query:
                os.system("start cmd")
            elif "open camera" in self.query:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam',img)
                    k = cv2.waitKey(50)
                    if k==27:
                        break
                cap.release()
                cv2.destroyAllWindows()
            elif "play music" in self.query:
                music_dir = "E:\music"
                songs = os.listdir(music_dir)
                #rd = random.choice(songs)
                for song in songs:
                    if song.endswith('.mp3'):
                     os.startfile(os.path.join(music_dir,song))

            
            elif "ip address" in self.query:
                ip = get('https://api.ipify.org').text
                speak(f"your IP address is {ip}")

            elif "wikipedia" in self.query:
                speak("searching wikipedia.....")
                self.query = self.query.replace("wikipedia","")
                results = wikipedia.summary(self.query, sentences=2)
                speak("according to wikipedia")
                speak(results)
                #print(results)

            elif "open youtube" in self.query:
                webbrowser.open("www.youtube.com")
            
            elif "open google" in self.query:
                speak("mam, what should i search on google")
                cm = self.takecommand().lower()
                webbrowser.open(f"{cm}")
            
            #elif "send message" in self.query:
                #kit.sendwhatmsg("+919921775503", "hi pallavi",00,00)
            
            elif "email to sonal" in self.query:
                try:
                    speak("What should i say?")
                    content = self.takecommand().lower()
                    to = "khardesonal18@gmail.com"
                    sendEmail(to,content)
                    speak("Email has been sent to sonal")

                except Exception as e:
                    print(e)
                    speak("Sorry Mam, I am not able to send mail")

            elif "no thanks" in self.query:
                speak("thaks for using me mam, have a good day")
                sys.exit()
            
            #to close my application
            elif "close notepad" in self.query:
                speak("okay mam, closing notepad")
                os.system("taskkill /f /im notepad.exe")
            
            elif "close youtube" in self.query:
                speak("okay mam, closing youtube")
                os.system("taskkill /f /im www.youtube.com")
            
            elif "close music" in self.query:
                speak("okay mam, closing music")
                os.system("taskkill /f /im music_dr")
                
            #10 stone paper scisorrs
            elif "game" in self.query:
                speak("choose among rock paper or scissor")
                voice_data = self.takecommand()
                
                moves=["rock", "paper", "scissor"]
            
                cmove=random.choice(moves)
                pmove=voice_data
                

                speak("The computer chose " + cmove)
                speak("You chose " + pmove)
                #engine_speak("hi")


                if pmove==cmove:
                    speak("the match is draw")
                elif pmove== "rock" and cmove== "scissor":
                    speak("Player wins")
                elif pmove== "rock" and cmove== "paper":
                    speak("Computer wins")
                elif pmove== "paper" and cmove== "rock":
                    speak("Player wins")
                elif pmove== "paper" and cmove== "scissor":
                    speak("Computer wins")
                elif pmove== "scissor" and cmove== "paper":
                    speak("Player wins")
                elif pmove== "scissor" and cmove== "rock":
                    speak("Computer wins")


            #to set alarm 
            elif "set alarm" in self.query:
                speak("mam pleease tell me the time to set alarm. for example, set alarm to 5:30 am")
                tt = self.takecommand()
                tt = tt.replace("set alarm to ","")
                tt = tt.replace(".","")
                tt.upper()
                MyAlarm.alarm(tt)

            elif 'volume up' in self.query:
                pyautogui.press("volumeup")

            elif 'volume dowm' in self.query:
                pyautogui.press("volumedown")

            elif 'volume mute' in self.query:
                pyautogui.press("volumemute")
            
            #to find a joke
            elif "tell me a joke" in self.query:
                joke = pyjokes.get_joke()
                speak(joke)

            elif "shut down the system" in self.query:
                os.system("shutdown /s /t 5")
            elif "restart the system" in self.query:
                os.system("shutdown /r /t 5")
            elif "sleep the system" in self.query:
                os.system("round123.exe powrprof.dll, SetSuspendState 0,1,0")
            
            ################################################################################
            elif 'switch the window'in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")

            elif "tell me news" in self.query:
                speak("please wait mam, fetching the latest news")
                news()
            ####################to read file################
            
            elif "read pdf" in self.query:
                pdf_reader()
            
            elif "do some calculations" in self.query or "can you calculate" in self.query:
                try:
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
                        speak("Say what you want to calculate, example: 3 plus 3")
                        print("listening.....")
                        r.adjust_for_ambient_noise(source)
                        audio = r.listen(source)
                    my_string = r.recognize_google(audio)
                    print(my_string)
                    def get_operator_fn(op):
                        return {
                            '+' : operator.add,
                            '-' : operator.sub,
                            'x' : operator.mul,
                            '/' : operator.__truediv__,

                        }[op]
                    def eval_binary_expr(op1, oper,op2):
                        op1,op2 = int(op1), int(op2)
                        return get_operator_fn(oper)(op1,op2)
                    speak("your result is")
                    speak(eval_binary_expr(*(my_string.split())))
                except Exception as e:
                    print(e)
                    speak("Sorry Mam")
            elif "temperature" in self.query:
                search = "temperature in Buldana"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text,"html.parser")
                temp = data.find("div", class_="BNeawe").text
                speak(f"current{search} is {temp}")
            
            elif "activate how to do mod" in self.query:
                from pywikihow import search_wikihow
                speak("how to do mode is activated please tell me what you want to know")
                how = self.takecommand()
                max_results = 1
                how_to = search_wikihow(how, max_results)
                assert len(how_to)==1
                how_to[0].print()
                speak(how_to[0].summary)
            
            elif "internet speed" in self.query:
                st = speedtest.Speedtest()
                dl = st.download()
                up = st.upload()
                speak(f"mam we have {dl} bit per second downloading speed and {up} bit per second uploading speed")



    ##########################################################################
            elif  "where we are" in self.query:
                speak("wait mam, let me check")
                try:
                    ipAdd = requests.get('https://api.ipify.org').text
                    print(ipAdd)
                    url ='https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                    geo_requests = requests.get(url)
                    geo_data =geo_requests.json()
                    city = geo_data['city']
                    country=geo_data['country']
                    speak(f"mam i am not sure, but i think we are in {city} city of {country}")
                except Exception as e:
                    speak("sorry mam, due to network issue i am not able to find where we are")
                    pass
                
            elif "instagram profile" in self.query:
                speak("sir please enter the user name correctly.")
                name = input("Enter username here:")
                webbrowser.open(f"www.instagram.com/{name}")
                speak(f"mam here is the profile of the user {name}")
                time.sleep(5)
                speak(f"mam would like to download profile picture of this account.")
                condition = self.takecommand().lower()
                if "yes" in condition:
                    mod = instaloader.Instaloader()
                    mod.download_profile(name, profile_pic_only = True)
                    speak("I am done sir, profile picture is saved in our main folder. now i am ready")
                else:
                    pass
                ###########################################
            elif "take a screenshot" in self.query:
                speak("mam, please tell me the name for this screenshot file")
                name = self.takecommand().lower()
                speak("please mam hold the screen for few seconds, i am taking screenshot")
                time.sleep(3)
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                speak("i am done mam, the screenshot is saved in our main folder. now i am ready for it")
                pass
            
            elif "hide all files" in self.query or "hide this folder" in self.query or "visible for everyone" in self.query:
                speak("mam please tell me you want to hide this folder or make it visible for everyone")
                condition = self.takecommand().lower()
                if "hide" in condition:
                    os.system("attrib +h /s /d")
                    speak("mam, all the files in this folder are now hidden")
                elif "visible" in condition:
                    os.system("attrib -h /s /d")
                    speak("mam, all the files in this folder are now visible to everyone. i wish you are taking")
                elif "leave it" in condition or "leave for now" in condition:
                    speak("ok mam")


            speak("mam, do you have any other work")
            ###################################################################



startExecution = MainThread()
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui= Ui_BarbieWithBrain()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie= QtGui.QMovie("C:/Users/LENOVO/Downloads/2RNb.gif") 
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()  

        self.ui.movie= QtGui.QMovie("C:/Users/LENOVO/Downloads/Jarvis_Loading_Screen.gif") 
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start() 
        timer =QTimer(self)
        timer.timeout.connect(self.showTime)   
        timer.start(1000)     
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        now = QDate.currentDate()
        label_time= current_time.toString('hh:mm:ss')
        label_date= now.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)

app = QApplication(sys.argv)
sonal = Main()
sonal.show()
exit(app.exec_())
        

