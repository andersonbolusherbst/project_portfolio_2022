import streamlit as st
import pandas as pd
import numpy as np
import requests

option = st.sidebar.selectbox("HAB LABS Services", ( "Home", 'Analytics', 'Data Infrastructure','Machine Learning','Custom Web Apps'))

st.markdown(
    """
<style>
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.css-163ttbj.e1fqkh3o11 > div.css-6qob1r.e1fqkh3o3{
background: #29abe2;
}
</style>
""",
    unsafe_allow_html=True,
)

if option == "Home":
  st.image("HAB LABS.png", width = 750)
  st.markdown("<h1 style='text-align: center; color: black;'>WE HELP COMPANIES GROW</h1>", unsafe_allow_html=True)
  st.write("")
  st.markdown("<h4 style='text-align: center; color: black;'>Welcome to the HAB LABS Digital Portfolio.</h4>", unsafe_allow_html=True)
  st.image("Team Mugshot.png", width = 750)

#if option == "Analytics":
  
#if option == "Data Infrastructure:
  
if option == "Machine Learning":
  st.image("Doggo.jpg")
  st.markdown("<h2 style='text-align: center; color: black;'>PetTech Company</h2>", unsafe_allow_html=True)
  st.write("")
  st.markdown("<h5 style='text-align: left; color: black;'>For this project we were tasked with using the raw data from a 3-axis accelerometer and a 3-axis gyroscope to classify the postion of a dog.</h5>", unsafe_allow_html=True)
  st.write("")
  st.markdown("<h5 style='text-align: left; color: black;'>For this use case our algorithim was required to be embedded on a device worn around the dogs neck from which various outputs would alert the dogs owner to any abnormal behaiviour (i.e Lying on side for too long).</h5>", unsafe_allow_html=True)
  
  st.write("---------")
  
  st.markdown("<h2 style='text-align: center; color: black;'>Data Gathering and Cleaning</h2>", unsafe_allow_html=True)
  st.write("")
  st.markdown("<h5 style='text-align: left; color: black;'>A crucial part of any Machine Laerning Project is data.</h5>", unsafe_allow_html=True)
  st.write("")
  st.markdown("<h5 style='text-align: left; color: black;'>In this example we were able to obtain a publically available dataset (see link to paper). We went through the appropriate data cleaning methodology and arrived at our dataframe which you can see below.</h5>", unsafe_allow_html=True)
  st.write("")
  st.markdown("<h5 style='text-align: left; color: black;'>We now had data with which to classify a dog into one of six positions (Sitting, Walking, Standing, Running, Lying down and Eating and drinking).</h5>", unsafe_allow_html=True)
  
  if st.button('Run Me and Explore Our Labelled Data Set'):
    @st.cache(allow_output_mutation=True)
    def load_data():
      a = pd.read_csv("dog_data (1).csv")
      return a
    df = load_data()
    st.dataframe(df)
    
  st.markdown("<h2 style='text-align: center; color: black;'>Model Selection</h2>", unsafe_allow_html=True)
  
  st.write("---------")
  
  
  st.markdown("<h2 style='text-align: center; color: black;'>Model Outcomes</h2>", unsafe_allow_html=True)
  st.markdown("<h3 stayle='text-align: left; color: black;'>A Classification report is used to measure the quality of predictions from a classification algorithm. How many predictions are True and how many are False.</h3>", unsafe_allow_html=True) 
  st.markdown("<h3 stayle='text-align: left; color: black;'>More specifically, True Positives, False Positives, True negatives and False Negatives are used to predict the metrics of a classification report as shown below.</h3>", unsafe_allow_html=True)
  st.markdown("<h4 style='text-align: left; color: black;'>🎯 Precision – What percent of your predictions were correct?</h4>", unsafe_allow_html=True)
  st.markdown("<h4 style='text-align: left; color: black;'>🎯 Recall – What percent of the positive cases did you catch?</h4>", unsafe_allow_html=True)
  st.markdown("<h4 style='text-align: left; color: black;'>🎯 F1 score – What percent of positive predictions were correct?</h4>", unsafe_allow_html=True)
  st.markdown("<h4 style='text-align: left; color: black;'>🎯 Support - How many predictions in each case</h4>", unsafe_allow_html=True)

  st.write("")
  st.markdown("<h3 style='text-align: center; color: black;'>XGBoost Model Results</h3>", unsafe_allow_html=True)
  st.markdown("<h4 style='text-align: left; color: black;'>The results after using the XGBoost Algorithm can be seen below. Overall accuracy 83%.</h4>", unsafe_allow_html=True)
  
   
  
  st.image("XGBoost Classification Report.png", width = 800)
  st.image("XGBoost.png", width = 800)

 
  st.markdown("<h3 style='text-align: center; color: black;'>Decision Tree Model Results</h3>", unsafe_allow_html=True)
  
  st.markdown("<h4 style='text-align: left; color: black;'>The results after using the Decision Tree Algorithm can be seen below. Overall accuracy 87%. We selected this model for reasons explained below</h4>", unsafe_allow_html=True)
  
  st.image("Decision Tree Classification Report.png", width = 800)
  st.image("Decision_Tree.png", width = 800)
  
  st.write("---------")
  
  st.markdown("<h2 style='text-align: center; color: black;'>Challenges</h2>", unsafe_allow_html=True)  
  
  st.write("---------")
  
  st.markdown("<h2 style='text-align: center; color: black;'>Video Walkthrough</h2>", unsafe_allow_html=True) 

  st.write("Check out our work here [link](https://colab.research.google.com/drive/1sjGgWWfqmBHteGup-PGr0A4XKCkhl8ZR?hl=en#scrollTo=xG55BCrpIwqk)")

  st.write("---------")  
  
 #if option == "Custom Web Apps":
