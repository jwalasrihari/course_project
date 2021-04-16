# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 18:51:14 2020

@author: Pc
"""

import speech_recognition as sr

def speech_to_text():
    r=sr.Recognizer()
    print('please talk')
    with sr.Microphone() as source:
        audio_data=r.record(source,duration=5)
        print('Recognizing....')
        text=r.recognize_google(audio_data)
        print(text)

#speech_to_text()