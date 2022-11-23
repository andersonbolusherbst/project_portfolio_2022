import streamlit as st
import pandas as pd
import numpy as np
import requests

st.image("Website.png", width=1000, height=1500)

option = st.sidebar.selectbox("HAB LABS Services", ('Analytics', 'Data Infrastructure','Machine Learning','Custom Web Apps'))

#if option == "Machine Learning":
