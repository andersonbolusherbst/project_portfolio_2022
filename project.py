import streamlit as st
import pandas as pd
import numpy as np
import requests

#from PIL import Image
#background = Image.open('Website.png')

option = st.sidebar.selectbox("HAB LABS Services", ( "Home", 'Analytics', 'Data Infrastructure','Machine Learning','Custom Web Apps'))

if option == "Home":

  col1, col2, col3 = st.columns([1,1,1])

  with col1:
    st.image("Website.png", width=900)

  with col2:
    st.write("")

  with col3:
    st.write("")

  st.markdown("<h1 style='text-align: center; color: black;'>WE HELP COMPANIES GROW</h1>", unsafe_allow_html=True)
  st.markdown("<h2 style='text-align: center; color: black;'>Become data-driven today and scale your business.We take the time to understand your business and how data can help you to achieve your goals.</h2>", unsafe_allow_html=True)


#if option == "Analytics":
  
#if option == "Data Infrastructure:
  
if option == "Machine Learning":
  st.markdown("<h1 style='text-align: center; color: black;'>PetTech Company</h1>", unsafe_allow_html=True)
  st.write("")
  st.markdown("<h4 style='text-align: left; color: black;'>For this project we were tasked with using the raw data from a 3-axis accelerometer and a 3-axis gyroscope to classify the postion of a dog.</h4>", unsafe_allow_html=True)
  st.write("")
  st.markdown("<h4 style='text-align: left; color: black;'>For this use case our algorithim was required to be embedded on a device worn around the dogs neck from which various outputs would alert the dogs owner to any abnormal behaiviour (i.e Lying on side for too long) .</h4>", unsafe_allow_html=True)
  
dog_data = pd.DataFrame("dog_data.csv")
  
if st.button('Run Me'):
    st.dataframe(dog_data)
  
  
  
  
  
  
  
  
  
  
  
  
  
 #if option == "Custom Web Apps":
