import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
from geotext import GeoText
import importlib
import convert_ttos
import convert_stot

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def talk(text):
    print(text)
    engine.say(text)
    engine.runAndWait()
    
def take_command():
    currentTime=datetime.datetime.now()
    if currentTime.hour < 12:
        talk('Good morning,i am alexa. How can i help you')
        
    elif 12 <= currentTime.hour < 18:
        talk('Good afternoon,i am alexa. How can i help you')
    else:
        talk('Good evening,i am alexa. How can i help you')
    try:
        with sr.Microphone() as source:
            print('listen...')
            voice=listener.listen(source)
            print('recogining...')
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
            if 'alexa' in command:
                command = command.replace('alexa','')
    except:
        pass
    return command
def run_alexa():
    command =take_command()
    if 'your name' in command:
        talk('my name is alexa')
    elif 'what can you do' in command:
        talk('I can play videos.I can say jokes and time.I can search in google')
    elif 'play' in command:
        song = command.replace('play','')
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('current time is'+ time)
    elif 'who is' in command:
        person = command.replace('who is','')
        info=wikipedia.summary(person,2)
        talk(info)
    elif 'joke' in command:
        joke1=pyjokes.get_joke()
        talk(joke1)
    elif 'located' in command or 'location' in command:
        command=command.replace('located','')
        command=command.title()
        places = GeoText(command)
        print(command)
        print(places.cities)
        webbrowser.open('https://www.google.com/maps/place/' + places.cities[0])
    elif 'where is' in command:
        url = "https://www.google.com.tr/search?q={}".format(command)
        webbrowser.open_new_tab(url)
    elif 'convert text to speech' in command:
        importlib.reload(convert_ttos)
        convert_ttos.text_to_speech()
    elif 'convert speech to text' in command:
        importlib.reload(convert_stot)
        convert_stot.speech_to_text()
    elif ' ' in command:
        term= command.replace('open in browser','')
        url = "https://www.google.com.tr/search?q={}".format(term)
        webbrowser.open_new_tab(url)
    else:
        talk('please come again')

run_alexa()     