import streamlit as st
import pandas as pd
import numpy as np
import requests

st.image("Website.png")

option = st.sidebar.selectbox("HAB LABS Services", ('Start Here','Analytics', 'Data Infrastructure','Machine Learning','Custom Web Apps'))


