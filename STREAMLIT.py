#Import all relevant libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore
from ydata_profiling import ProfileReport
from ipyvizzu import chart, Data, Config
import streamlit as st
from PIL import Image


 # ------ PAGES -----
st.image('toyo.png') 


st.title('How :red[Toyota] dominate Saudi Arabia Market?')
# st.title('_Streamlit_ is :red[TEST] :sunglasses:')
cars = pd.read_csv("Data\cars.csv")
# ---
st.text("At the beginning of Toyota's entry into the car market,")
st.text("it showed considerable growth locally.") 
st.text("The next figure will demonstrate Toyota's impact in Saudi Arabia .")

# ---
image = Image.open("IMAGE.png")
st.image(image, caption="Figure 1. ' This figure shown the most sell cars by region ' ", use_column_width=True)
# ---------

# Create a bar chart
st.header("( YOU ARE WHAT DRIVE US )")
st.text("One of the slogans that Toyota used frequency")
st.text("We can see in the chart below that Toyota have been in every city in Saudi Arabia") 
st.text("Most cars sells by cities")
region_counts = cars['Region'].value_counts()
st.bar_chart(region_counts)

# ---

# Scatter graph 
toyotacars = cars[(cars['Make']=='Toyota')]

if "df" not in st.session_state:
    st.session_state.df = toyotacars

st.header("1978 IS THE START OF AN ERA")
st.text("From the below chart we can see toyota have been here from the beginning")
color = st.color_picker("Color", "#FF0000")
st.divider()

st.session_state.df["Year"] = st.session_state.df["Year"].astype(str)
st.scatter_chart(st.session_state.df, x="Year", y="Price", color=color)


#-----------------------

st.title('Conclusion')
st.text("Toyota, the company that grows with us and continues to write its success story.")
