import streamlit as st
import pandas as pd
import numpy as np
import requests

#from PIL import Image
#background = Image.open('Website.png')

col1, col2, col3 = st.columns([1,1,1])

with col1:
  st.image("Website.png", width=900)

with col2:
  st.write("")

with col3:
  st.write("")

st.markdown("<h1 style='text-align: center; color: black;'>WE HELP COMPANIES GROW</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: black;'>Become data-driven today and scale your business.We take the time to understand your business and how data can help you to achieve your goals.</h2>", unsafe_allow_html=True)

option = st.sidebar.selectbox("HAB LABS Services", ('Analytics', 'Data Infrastructure','Machine Learning','Custom Web Apps'))

#if option == "Machine Learning":
