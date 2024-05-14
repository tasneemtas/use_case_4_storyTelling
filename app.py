import streamlit as st
import pandas as pd

st.title('Our dataset:')

df = pd.read_csv("../../../Data/data_saudi_used_cars.csv")

st.dataframe(df)