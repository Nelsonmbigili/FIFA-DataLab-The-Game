import streamlit as st
from PIL import Image
import pandas as pd


# Loading Animation
with st.spinner('Loading page...'):
    # Page Title and Subtitle
    st.title("⚽ Fifa Data Lab: The Game")
    st.subheader(":violet[Predicting Football Players' Salaries]")
    st.subheader(":violet[A Data-Driven Approach]")
    
    # Display Image
    image_path = Image.open("./Assets/france.png") 
    st.image(image_path)

    # Objective Section
    st.markdown("### :violet[Objective]")
    st.write("Users can use this app to examine datasets from FIFA 17 to FIFA 22, spanning the years between 2017 and 2022. Using a linear regression model users can predict the salaries and market values of certain players using attributes such as their ratings on the game. The app allows fans of the game of football to make interesting observations about their favorite players using accurate data.")

    # Inspiration Section
    st.markdown("### :violet[Inspiration]")
    st.write("The FIFA games have been a crucial part of many of our lives and even some of the players actively keep up with how their performance on the pitch impacts their FIFA rating. This app was made to merge our collective love for football with data analysis to make some fun predictions about our favorite players.")


    # Our Dataset Section
    st.markdown("### :violet[Our Dataset]")
    st.write("The dataset we have selected includes data from six different versions of the game released between the years 2017 and 2022. The dataset is quite extensive and includes various attributes about the players including skills, physical attributes, potential ratings, wages, and market values. As a result this dataset will help us make accurate predictions about all the players.") 
    st.markdown("##### :red[Dataset Columns:]")
    df = pd.read_csv("Datasets/FIFA22_official_data.csv")
    st.code(
    '''
    ID, Name, Age, Nationality, Overall, Potential, Club, Value(€M), Wage(€K), 
    Preferred Foot, International Reputation, Weak Foot, Skill Moves, Jersey Number, 
    Joined(yr), Contract Valid Until, Height(cm), Weight(kg), Crossing, Finishing, 
    HeadingAccuracy, ShortPassing, Volleys, Dribbling, Curve, FKAccuracy, LongPassing, 
    BallControl, Acceleration, SprintSpeed, Agility, Reactions, Balance, ShotPower, 
    Jumping, Stamina, Strength, LongShots, Aggression, Interceptions, Positioning, 
    Vision, Penalties, Composure, StandingTackle, SlidingTackle, GKDiving, GKHandling, 
    GKKicking, GKPositioning, GKReflexes, Best Overall Rating''', 
    language='python'
)


    # Our Goal Section
    st.markdown("### :violet[Our Goal]")
    st.write("Our main goal is to create an interactive and user-friendly application that provides valuable insights into FIFA player data. The app will allow users to:")
    st.write("- Preview raw data and explore different player attributes.")
    st.write("- Visualize player statistics and trends using interactive charts.")
    st.write("- Use a machine learning model to predict player salaries and market values.")
    st.write("By integrating data analytics and machine learning, we aim to make FIFA player analysis accessible to everyone, from casual gamers to data science enthusiasts.")

    # Final Message
    st.success("Let's dive into the world of FIFA data and uncover hidden insights together! ⚽")
