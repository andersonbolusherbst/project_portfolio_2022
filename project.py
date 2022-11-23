import streamlit as st
import pandas as pd
import numpy as np
import requests

from PIL import Image
background = Image.open('Website.png')
st.image(background, width=1920)

option = st.sidebar.selectbox("HAB LABS Services", ('Analytics', 'Data Infrastructure','Machine Learning','Custom Web Apps'))

#if option == "Machine Learning":
