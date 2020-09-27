# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 17:32:40 2020

@author: Harshita Phophalia
Project Name: BMi Web app
"""

import streamlit as st
from PIL import Image

st.title('Welcome to BMI Calculator')

#BMI Image
img=Image.open('bmi.jpg')
st.image(img,width=700)

h_mode=0

#Weight
weight=st.number_input("Enter your weight(in kgs")

#height
status=st.radio("Select your height format:",('cms','mts','feet'))

if(status=='cms'):
    h_mode=0
    height=st.number_input('Centimeteres')
elif(status=='mts'):
    h_mode=1
    height=st.number_input('Meteres')
else:
    h_mode=2
    height=st.number_input('Feet')
    
    
    
if(st.button('Calculate BMI')):
    if(h_mode == 0):
        bmi = weight / ((height/100)**2)
        
        
    elif(h_mode == 1):
        bmi = weight / (height ** 2)
        
    else:
        # 1 meter = 3.28
        bmi = weight / (((height/3.28))**2)
        
        
        
    if(bmi < 16):
        st.error('You are extremely underweight')
    elif(bmi >=16 and bmi < 18.5):
        st.warning('You are underweight')
    elif(bmi >=18.5 and bmi < 25):
        st.success('Healthy')
        st.balloons()
    elif(bmi >=25 and bmi < 30):
        st.warning('Overweight')
    elif(bmi >=30):
        st.error('Extremely Overweight')