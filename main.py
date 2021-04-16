# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 14:36:06 2020

@author: Pc
"""
import convert_ttos
import convert_stot
import puba
print('1.conversion of text to speech\n2.conversion to speech to text\n 3.virtual assitant\n 4.Exit')
temp=0
while(temp==0):
    n=int(input())
    if n==1:
        convert_ttos.text_to_speech()
    elif n==2:
        convert_stot.speech_to_text()
    elif n==3:
        puba.run_alexa() 
    elif n==4:
        temp==1