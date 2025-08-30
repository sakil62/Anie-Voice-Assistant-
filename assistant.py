import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import pywhatkit as kit
from keyboard import press
from keyboard import press_and_release
from keyboard import write
import pyjokes
import sys
import requests, json
from bs4 import BeautifulSoup
import cv2
import psutil
import speedtest
import time
import PyPDF2
import googletrans
import gtts
import playsound


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 125)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
        
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
        
    else:
        speak("Good Evening!")    
        
    speak("I am Anny. Please tell me sir how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        query = query.lower()
        print("User said:{}".format(query))
        #if 'english' in query:
         #   query = "en"
        #if 'bengali' in query:
         #   query = "bn"
        #if 'tamil' in query:
         #   query = 'ta'
        #if 'hindi' in query:               #NOT WORKING
          #  query = "hi"
        #if 'telegu' in query:
         #   query = 'te'
        #if 'spanish' in query:
         #   query = 'es'
        #if 'japanese' in query:
         #   query = 'ja'
        #if 'arabic' in query:
         #   query = 'ar'
            
    except Exception as e:
        #print(e)   
        print("You are not audible. Please say it again...")        
        return "None"
    return query  

#def trans():
    #recognizer = sr.Recognizer()
    #input_lang="bn"
    #output_lang="en"
    #translator = googletrans.Translator()
    
   # speak('what is input language')
   # input_lang = takeCommand()
   # speak('what is output language')
   # output_lang = takeCommand()
   
    #while (True):
        #try:
    
           # with sr.Microphone() as source:
                #print('Speak Now')
                #speak('speak now')
                #voice = recognizer.listen(source)
                #text = recognizer.recognize_google(voice, language=input_lang)
                #print(text)
                
                
                #translator = googletrans.Translator()
                #translation = translator.translate(text, dest=output_lang)
                #print(translation.text)
                
                #converted_audio = gtts.gTTS(translation.text, lang=output_lang)
                #converted_audio.save("hello.mp3")
                #playsound.playsound("hello.mp3")
        
        #except:
            #pass
      
        #translated = translator.translate(text, dest=output_lang)
        #print(translated.text)
        #talk(translated.text)
        #converted_audio = gtts.gTTS(translated.text, lang=output_lang)
        #converted_audio.save('romantic.mp3')
        #playsound.playsound('romantic.mp3')
        # print(googletrans.LANGUAGES)
        #os.remove("romantic.mp3")
        #ans=input('Enter z to keep speaking \n Enter x to swap language \n Enter a to stop \n')
        #if ans=="z":
         #   continue
        #elif ans=='x':
           # tk=input_lang
          #  input_lang=output_lang
         #   output_lang=tk
        #elif ans == 'a':
          #  break

def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apikey=83263a48521a48a797182dbc3926e513'

    main_page = requests.get(main_url).json()
    #print(main_page)
    articles = main_page["articles"]
    #print(articles)
    head = []
    day=["first","second","third","fourth","fifth","sixth","seventh","eighth","nineth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        print(f"today's {day[i]} news is: ", head[i])
        speak(f"today's {day[i]} news is: {head[i]}")
        
def pdf_reader():
    book = open('DBMS.pdf','rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    print(f"Total numbers of pages in this book {pages} ")
    speak(f"Total numbers of pages in this book {pages} ")
    speak("sir please enter the page number which i have to read")
    num = int(input("Please enter the page number i have to read: "))
    #page = pdfReader.getPage(pg)
    #text = page.extractText()
    speaker = pyttsx3.init()
    for num in range(num, pages):
        page = pdfReader.getPage(num)
        text = page.extractText()
        speaker.say(text)
        speaker.runAndWait()
    #print(text)
    #speak(text)
    
    
    
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
    
    
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)    
            
        elif 'play music' in query:
            n = random.randint(0,284)
            print(n)
            music_dir = 'C:\\Users\\hp\\Music\\SONG'    
            song = os.listdir(music_dir)
            print(song)
            os.startfile(os.path.join(music_dir, song[n])) 
                                    
        elif 'open google' in query:
            webbrowser.open("google.com")
            
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
            
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
           
        elif 'open twitter' in query:
            webbrowser.open("twitter.com")                
            
        elif 'open' in query:
            result = webbrowser.open(query)      
         
        elif 'search' in query:
            kit.search(query)   
        
        #For Youtube---------------------------    
        
        elif 'youtube' in query:
            kit.playonyt(query)
            
        elif 'pause' in query:
            press('space bar')
            
        elif 'resume' in query:
            press('space bar')  
            
        elif 'play' in query:
            press('space bar')     
            
        elif 'full screen' in query:
            press('f')
            
        elif 'small screen' in query or 'half screen' in query:
            press('t')    
            
        elif 'skip' in query:
            press('l')
            
        elif 'back' in query:
            press('j')
            
        elif 'increase playback speed' in query:
            press_and_release('SHIFT + .')
            
        elif 'decrease playback speed' in query:
            press_and_release('SHIFT + ,')
            
        elif 'previous video' in query:
            press_and_release('SHIFT + p')
            
        elif 'next video' in query:
            press_and_release('SHIFT + n')
            
        elif 'mute' in query:
            press('m') 
            
        elif 'unmute' in query:
            press('m') 
        #-------------------------------------
        
        elif 'joke' in query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)  
            
        elif "date" in query or "what is today's date" in query:
            date = datetime.datetime.today().strftime('%d:%B %Y ')
            print('today is ' + date)
            speak('today is ' + date)
            
        elif 'time' in query or "what is the time now" in query:      
            time = datetime.datetime.now().strftime('%I:%M %p')
            print('time is ' + time)
            speak('time is ' + time)
            
        elif "tell me news" in query:
            speak("please wait sir, fetching the latest news")
            news()  
            
       # elif 'translate' in query:
        #    trans()
        
        #FOR SYSTEM---------------- 
        
        elif "how much battery left" in query or "battery" in query or "how much battery you have" in query:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            print(f"sir our system have {percentage} percent battery")
            speak(f"sir our system have {percentage} percent battery")
            
        elif "notepad" in query:
            npath = "c:\\Windows\\System32\\notepad.exe"
            os.startfile(npath)
            
        elif "command prompt" in query or "cmd" in query:
            os.system("start cmd") 
            
        elif "close notepad" in query:
            speak("okay sir, closing notepad")               #NOT WORKING
            os.system("taskkill /f /im notepad.exe")
           
        elif "shut down the system" in query:
            os.system("shutdown /s /t 5")
            
        elif "restart down the system" in query:
            os.system("shutdown /r /t 5")          
        
        elif 'ip address' in query:
            ip = requests.get('https://api.ipify.org').text
            print(ip)
            speak(f"Your ip address is {ip}")  
            
        elif "inetrnet speed" in query or "our internet speed" in query or "tell me internet speed" in query:
            st = speedtest.Speedtest()
            dl = st.download()                    #NOT WORKING
            up = st.upload()
            print(f"sir we have {dl} bit per second downloading speed and {up} bit per second uploading speed")
            speak(f"sir we have {dl} bit per second downloading speed and {up} bit per second uploading speed")
        
        elif "temperature" in query or "what is the temperature now" in query:
           #search = "temperature in Kolkata"
            search = takeCommand().lower()
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            print(search, temp)
            speak(f"current {search} is {temp}")   
            
        elif "send message" in query:
            speak('what is mobile number...')
            ph = takeCommand().lower()
            print(ph)
            speak(f'mobile number is... {ph}')
            speak('what is the message?')
            sms = takeCommand().lower()
            print(sms)
            kit.sendwhatmsg(f"+91{ph}", f"{sms}",2,25)      
            
        elif "where i am" in query or "where we are" in query or "my location" in query or "what is my location" in query:
            speak("wait sir, lem me check")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_requests = requests.get(url)   
                geo_data = geo_requests.json()
                #print(geo_data)
                city = geo_data['city']
                #state = geo_data['state']
                country = geo_data['country']
                print(f"sir i am not sure, but i think we are in {city} city of {country} country")
                speak(f"sir i am not sure, but i think we are in {city} city of {country} country")
            except Exception as e:
                speak("Sorry sir, Due to network issue i am not able to find your location")
                pass
        
        elif "read pdf" in query:
            pdf_reader()
        
        #-------------------
                
        elif 'tell me about yourself' in query:
            speak('My name is Anny. I am your voice assistant')        
                
        elif 'how are you' in query:
            speak('I am fine sir')
            
        elif 'thank you' in query:
            speak('You are welcome')
            
                          
        
                
                
        elif "goodbye" in query or "offline" in query or "bye" in query or "stop" in query:
                speak("Alright sir, going offline. It was nice working with you")
                sys.exit()   
                
        