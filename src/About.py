import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
from PIL import Image
import codecs
import streamlit.components.v1 as components
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import matplotlib.pyplot as plt

with st.spinner('Loading page...'):
    st.title("Fifa Data Lab: The Game")
    st.subheader(":violet[Predicting Football Player's Value and Salary: Data Driven Approach]")
    image_path = Image.open("./Assets/fifa_logo.png") 
    st.image(image_path)




    st.markdown("<h3 style='text-align: center; font-weight: bold;'>Objective</h3>", unsafe_allow_html=True)
    st.write("""
Understanding the evolution of player performance in FIFA is crucial for scouts, gamers, and analysts. 
By analyzing historical FIFA data from 2017 to 2023, we aim to uncover key trends and predict crucial 
player attributes using linear regression.

Our model will help in:
- Identifying undervalued players based on predicted ratings.
- Analyzing trends in player development over time.
- Supporting team-building decisions in FIFA career mode.
""")

    st.markdown("<h3 style='text-align: center; font-weight: bold;'>Inspiration</h3>", unsafe_allow_html=True)

    st.markdown("<h3 style='text-align: center; font-weight: bold;'>Our Dataset</h3>", unsafe_allow_html=True)

    st.markdown("<h3 style='text-align: center; font-weight: bold;'>Our Goal</h3>", unsafe_allow_html=True)
