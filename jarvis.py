from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from time import time_ns
from pywhatkit.mail import send_mail
import requests
from requests.api import request
import win32api
import pyttsx3
import speech_recognition as sr
import datetime
import PyPDF2
import os
import numpy as np
import cv2
import winsound
import random
from requests import get
import wikipedia
import webbrowser
import instaloader
import pywhatkit as kit
import smtplib
import sys
import pyautogui as p
import time
import pyjokes
import pyautogui
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
import jarvisUi
from jarvisUi import Ui_MainWindow
from os import environ
import operator
from bs4 import BeautifulSoup
from pywikihow import search_wikihow

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0] .id)
engine.setProperty('rate', 180)

# text to speech


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    print(audio)

def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def alarm(timing):
    alttime = str(datetime.datetime.now().strptime(timing, "%I:%M %p"))
    alttime = alttime[11:-3]
    hreal = alttime[:2]
    hreal = int(hreal)
    mreal = alttime[3:5]
    mreal = int(mreal)
    speak(f"Done, Alarm is set for {timing}")

    while True:
        if hreal == datetime.datetime.now().hour:
            if mreal == datetime.datetime.now().minute:
                print("Alarm is running")
                winsound.PlaySound('abc', winsound.SND_LOOP)
            elif mreal < datetime.datetime.now().minute:
                break


def wish():
    h = int(datetime.datetime.now().hour)
    time = datetime.datetime.now()
    tt = time.strftime("%I:%M %p")
    if(0 <= h < 12):
        speak(f"Good Morning sir, it's {tt}")
    elif(12 <= h < 17):
        speak(f"Good Afternoon sir, it's {tt}")
    elif(17 <= h < 20):
        speak(f"Good Evening sir, it's {tt}")
    elif(20 <= h < 24):
        speak(f"Good night sir, it's {tt}")


def sendMail(to, content, gmail, password):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail, password )
    server.sendmail(gmail, to, content)
    server.close()


def pdf_Reader():
    book = open(
        resource_path("C:\\Users\\Karan Patel\\Desktop\\KpPython\\.vscode\\jarvis\\machine_learning_tutorial.pdf"), "rb")
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speak(f"Total number of pages in this book {pages}")
    speak("Sir please enter the page number into shell i have to read")
    page = int(input("Enter Page NUmber Here : "))
    pg = pdfReader.getPage(page)
    text = pg.extractText()
    speak(text)


def suppress_qt_warning():
    environ["QT_DEVICE_PIXEL_RATION"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"


def news():
    main_url = "http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=953e8108b0204764a456a727c7764939"
    main_page = requests.get(main_url).json()
    articles = main_page['articles']
    head = []
    day = ["First", "Second", "Third", "Fourth", "Fifth"]
    for i in articles:
        head.append(i['title'])
    for i in range(len(day)):
        speak(f"today's {day[i]} news is {head[i]}")


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()
    
    

    def run(self):
        speak("Please say wake up to continue")
        while True:
            self.query = self.takeCommand()
            if "wake up" in self.query or "hello" in self.query or "are you there" in self.query:
                self.TaskExecution()

          
    def takeCommand(self):
        r = sr.Recognizer()
        self.query = ""
        with sr.Microphone() as source:
            print("Listening...........")
            r.pause_threshold = 1
            audio = r.listen(source, timeout=1, phrase_time_limit=7)

        try:
            print("Recognizing......")
            self.query = r.recognize_google(audio, language='en-in')
            print(f"User Said : {self.query}")

        except Exception as e:
            #speak("Say That again please......")
            return("none")
        return self.query
 
    def TaskExecution(self):
        wish()
        speak("I am Jarvis How may i help you?")
        while True:
            self.query = self.takeCommand().lower()
            if "open notepad" in self.query:
                os.startfile(
                    resource_path("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Notepad++"))
            elif "open vs code" in self.query:
                os.startfile(resource_path
                    ("C:\\Users\\Karan Patel\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"))
            elif "open command prompt" in self.query:
                os.system("start cmd")
            elif "open camera" in self.query:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow("Sweety's Camera", img)
                    k = cv2.waitKey(50)
                    if k == 27:
                        break
                cap.release()
                cv2.destroyAllWindows()
            elif "play music" in self.query:
                os.startfile(resource_path("Wafa Na Raas Aayee.mp3"))
            elif "ip address" in self.query:
                ip = get("https://api.ipify.org").text
                speak(f"your ip address is {ip}")
            elif "wikipedia" in self.query:
                speak("Serching Wikipedia.....")
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences=2)
                speak("According to wikipedia...")
                speak(results)
            elif "open youtube" in self.query:
                webbrowser.open("youtube.com")
            elif "open facebook" in self.query:
                webbrowser.open("facebook.com")
            elif "stack overflow" in self.query:
                webbrowser.open("stackoverflow.com")
            elif "open google" in self.query:
                speak("What i should sheach on google ?")
                s = self.takeCommand().lower()
                webbrowser.open(f"{s}")
            elif "send whatsapp message" in self.query:
                #speak("Please tell me message..")
                # s=self.takeCommand()
                t = datetime.datetime.now()
                time = t + datetime.timedelta(minutes=1)
                speak("Please Enter Number with country code in shell")
                num=input("Enter Number here: ")
                kit.sendwhatmsg(
                    num, "Hello How Are You?", int(time.hour), int(time.minute))
            elif "play songs on youtube" in self.query:
                speak("please tell me song name..")
                s = self.takeCommand().lower()
                kit.playonyt(s)
            elif "send mail" in self.query:
                speak("Enter Your Gmail id and password in shell")
                gmail=input("Enter Gmail Id: ")
                password1=input("Enter Your Paasword: ")
                speak("Sir What should i say")
                self.query = self.takeCommand().lower()
                if "send a file" in self.query:
                    speak("Enter gmail id of receiver in shell")
                    send_to = input("Enter gmail id here")
                    speak("Ok sir, What is the subject for this mail?")
                    self.query = self.takeCommand().lower()
                    subject = self.query
                    speak("And sir what is the message for this mail?")
                    self.query2 = self.takeCommand().lower()
                    message = self.query2
                    speak(
                        "Sir Please Enter the correct Path of the File into shell..  ")
                    file = input("Enter Path Location Here : ")

                    speak("Please Wait I Am Sending Mail Now")
                    msg = MIMEMultipart()
                    msg['From'] = gmail
                    msg['To'] = send_to
                    msg['Subject'] = subject

                    msg.attach(MIMEText(message, 'plain'))

                    fn = os.path.basename(file)
                    attachment = open(file, "rb")
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition',
                                    "attachment : fn %s" % fn)

                    msg.attach(part)

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login(gmail, password1)
                    text = msg.as_string()
                    server.sendmail(gmail,send_to, text)
                    server.close()
                    speak("Mail Sent Successfully")
                else:
                    try:
                        speak("Enter gmail id of receiver in shell")
                        send_to = input("Enter gmail id here")
                        speak("please tell me message for mail")
                        content = self.takeCommand().lower()
                        sendMail(send_to, content, gmail, password1)
                        speak("Email sent suceessfully")
                    except Exception as e:
                        speak("Sorry Email has not sent")
            elif "you can sleep" in self.query or "sleep now" in self.query:
                speak("Okay sir, I am going to sleep you can call me anytime")
                self.wake()
                break
            elif "close notepad" in self.query:
                speak("Closing  Notepad")
                os.system("TASKKILL /F /IM notepad++.exe")
            elif "close faceboook" in self.query:
                speak("Closing  Facebook")
                os.system("TASKKILL /F /IM iexplore.exe")
            elif "close vs code" in self.query:
                speak("Closing VS code")
                os.system("TASKKILL /F /IM Code.exe")
            elif "close youtube" in self.query:
                speak("Closing  Youtube")
                os.system("cd C:\\Windows\\System32")
                os.system("TASKKILL  /F /IM iexplore.exe")
            elif "close command prompt" in self.query:
                speak("Closing  command prompt")
                os.system("TASKKILL  /F /IM cmd.exe")
            elif "tell me a joke" in self.query:
                joke = pyjokes.get_joke()
                speak(joke)
            elif "shut down" in self.query:
                os.system("shutdown /s /t 1")
            elif "restart" in self.query:
                os.system("shutdown /r /t 1 ")
            elif "sleep system" in self.query:
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
            elif "switch window" in self.query:
                speak("Switching Window")
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                time.sleep(.2)
                pyautogui.keyUp('alt')
            elif "tell me news" in self.query:
                speak("Please Wait sir, fetching the latest news...")
                news()
            elif "can you calculate" in self.query or "some calculation" in self. query:
                r = sr.Recognizer()
                try:
                    with sr.Microphone() as source:
                        speak("Say What you want to calculate? like 3 plus 3")
                        print("Listening.......")
                        r.adjust_for_ambient_noise(source)
                        audio = r.listen(source)
                        my_string = r.recognize_google(audio)
                        print(my_string)

                    def get_operator_fn(op):
                        return{
                            '+': operator.add,
                            '-': operator.sub,
                            'x': operator.mul,
                            'divide': operator.__truediv__
                        }[op]

                    def eval_binary_exp(op1, oper, op2):
                        op1, op2 = int(op1), int(op2)
                        return get_operator_fn(oper)(op1, op2)
                    st = eval_binary_exp(*(my_string.split()))
                    speak("Your result is ")
                    speak(st)
                except Exception as e:
                    speak("I can't do that calculation please try again")
            elif "can you tweet" in self.query:
                speak("sir, please enter your twitter gmail id and password in shell..")
                gmailid=input("enter gmail id here: ")
                password2=input("enter your password here: ")
                speak("Ok sir, What should i tweet?")
                s = self.takeCommand()
                speak("Ok sir, Tweet is posting")
                import twitterbot
                twitterbot.tweet(s,gmailid,password2)
                time.sleep(4)
                speak("Tweet Posted Successfully ")
            elif "where i am" in self.query or "where we are" in self.query:
                speak("Let me check")
                try:
                    ip = requests.get('https://api.ipify.org').text
                    print(ip)
                    url = 'https://get.geojs.io/v1/ip/geo/'+ip+'.json'
                    geo_req = requests.get(url)
                    geo_dat = geo_req.json()
                    city = geo_dat['city']
                    # state=geo_dat['state']
                    country = geo_dat['country']
                    speak(
                        f'Sir i am not sure, but i think we are in {city} city of {country} country')
                except Exception as e:
                    speak(
                        'Sorry sir, Due to network issue i am not able to find where we are.')
                    pass
            elif "instagram profile" in self.query or "profile in instagram" in self.query:
                speak("Sir, Please Enter Username in Shell..")
                us = input("Enter username here : ")
                webbrowser.open(f"www.instagram.com/{us}")
                speak(f"Sir Here is the profile of the user, {us}")
                import time
                time.sleep(4)
                speak(
                    "Sir Would You like to download profile picture of this account")
                cond = self.takeCommand().lower()
                if "yes" in cond:
                    test = instaloader.Instaloader()
                    test.download_profile(us, profile_pic_only=True)
                    speak(
                        "I am done sir, profile pic is saved in our main folder")
            elif "screenshot" in self.query:
                speak("Sir please tell me name for this screenshot file")
                name = self.takeCommand().lower()
                speak("Sir hold the screen for few second, i am taking screenshot")
                time.sleep(3)
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                speak("I am done sir, the screenshot saved in our main folder ")
            elif "read pdf" in self.query:
                pdf_Reader()
            elif "thank you" in self.query or "thanks" in self.query:
                speak("It's my pleasure sir")
            elif "hide all files" in self.query or "hide this folder" in self.query or "visible for everyone" in self.query:
                speak(
                    "sir, please tell me you want to hide this folder or make it visible to everyone")
                con = self.takeCommand(self).lower()
                if("hide" in con):
                    os.system("attrib +h /s /d")
                    speak("sir, all the files in this folder are now hidden")
                elif("visible" in con):
                    os.system("attrib -h /s /d")
                    speak(
                        "sir, all the files in this folder are now visible to everyone.i wish that you are taking this decision in peace")
                elif("leave it" in con):
                    speak("ok sir")
            elif "hello jarvis" in self.query:
                speak("Hello Sir, How may i help you?")
            elif "how are you" in self.query:
                speak("Sir, I am fine. What about you?")
            elif "i am fine" in self.query:
                speak("that's great to here from you  what can i do for you?")
            elif "temperature" in self.query:
                search = "temperature in ahmedabad"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                temp = data.find("div", class_="BNeawe").text
                speak(f"current {search} is {temp}")
            elif "activate how to do mode" in self.query:
                speak("how to do mode is activated please tell me what you want to know")
                how = self.takeCommand().lower()
                try:
                    if "close moode" in how or "exit" in how:
                        speak("how to do mode is closed")
                        break
                    else:
                        max_result = 1
                        how_to = search_wikihow(how, max_result)
                        assert len(how_to) == 1
                        how_to[0].print()
                        speak(how_to[0].summary)
                except Exception as e:
                    speak("Sorry sir, Can't Search that check network or change topic")
            elif "how much power left" in self.query or "how much power we have" in self.query or "battery" in self.query:
                import psutil
                battery = psutil.sensors_battery()
                pr = battery.percent
                speak(f"Sir our system have {pr} percent battery")
                if(pr >= 75):
                    speak("We have enough power to continue our work")
                elif(30 < pr < 75):
                    speak(
                        "We should connect our system to charging point to charge our battery")
                elif(15 <= pr <= 30):
                    speak("We don't have enough power to work, please connect charging")
                elif pr < 15:
                    speak(
                        "we have very low power, please connect charging otherwise system shutdown very soon")
            elif "internet speed" in self.query:
                import speedtest
                st = speedtest.Speedtest()
                dl = st.download()
                ul = st.upload()
                speak(
                    f"sir we have {dl} bit per second downloading speed and {ul} bit per second uploading speed")
            elif "send message" in self.query:
                speak("sir what should i send?")
                msg = self.takeCommand().lower()
                from twilio.rest import Client
                account_sid = "AC7b129274e0e0e767a2bf07307c433863"
                auth_token = "0d50a084ff48a5d7312f00cce9a9e1ef"
                client = Client(account_sid, auth_token)

                message = client.messages \
                    .create(
                        body=msg,
                        from_='+19384441823',
                        to='+916353736884'
                    )

                print(message.sid)
                speak("Sir, Message has been sent")
            elif "make a call" in self.query:
                speak("sir what should i tell on a call?")
                msg = self.takeCommand().lower()
                from twilio.rest import Client
                account_sid = "AC7b129274e0e0e767a2bf07307c433863"
                auth_token = "0d50a084ff48a5d7312f00cce9a9e1ef"
                client = Client(account_sid, auth_token)

                message = client.calls \
                    .create(
                        twiml="f'<Response><Say>{msg}</Say></Response>'",
                        from_='+19384441823',
                        to='+916353736884'
                    )

                print(message.sid)
                time.sleep(8)
                speak("Sir, Call has been completed")
            elif "volume down" in self.query or "decrease volume" in self.query:
                pyautogui.press("volumedown")
            elif "volume up" in self.query or "increase volume" in self.query:
                pyautogui.press("volumeup")
            elif "mute" in self.query:
                pyautogui.press("volumemute")
            elif "set alarm" in self.query:
                speak(
                    "sir please tell me the time to set alarm. for example set alarm to 2:40 AM")
                s = self.takeCommand().lower()
                s = s.replace("set alarm to ", "")
                s = s.replace(".", "")
                s = s.upper()
                print(s)
                alarm(s)
            elif "open mobile camera" in self.query:
                speak("Please install IP webcam app in your mobile")
                speak("And after open it enter your http ip address in shell")
                ip=input("Enter Ip Address here : ")
                import urllib.request
                import cv2
                import numpy as np
                import time
                url = ip + "/shot.jpg"
                while True:
                    img_arr = np.array(
                        bytearray(urllib.request.urlopen(url).read()), dtype=np.uint8)
                    img = cv2.imdecode(img_arr, -1)
                    cv2.imshow('IPWebcam', img)
                    q = cv2.waitKey(1)
                    if q == ord("q"):
                        break
                cv2.destroyAllWindows()
            else:
                speak("sir, can't understand your work please speak again")
            speak("Sir, now i am ready for other work")

    def wake(self):
        while True:
            permission = self.takeCommand().lower()
            if "wake up" in permission:
                self.TaskExecution()
            elif "goodbye" in permission:
                speak("Thanks for using me, Have a good day")
                sys.exit()

        


startExecution = MainThread()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie(resource_path("label4.gif"))
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie(resource_path("label6.gif"))
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        now = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = now.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)



suppress_qt_warning()
app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
sys.exit(app.exec_())

