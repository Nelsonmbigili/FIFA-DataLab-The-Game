import streamlit as st
from PIL import Image


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
    st.write("### Objective")
    st.write("This application is designed to explore player attributes from EA Sports' FIFA datasets across 6 years (2017-2022). Users can interactively analyze the data, visualize trends, and use a simple Linear Regression model to predict player salaries and market values. Whether you are a football fan, a data enthusiast, or just curious about player statistics, this app provides an engaging way to understand and explore FIFA data.")

    # Inspiration Section
    st.write("### Inspiration")
    st.write("We are passionate football fans who love and enjoy the game. FIFA has been a major part of our lives, bringing football closer to millions worldwide. With this project, we aim to merge our love for football with data analysis, helping users gain insights into how player attributes influence salaries and market values.")

    # Our Dataset Section
    st.write("### Our Dataset")
    st.write("The dataset consists of six FIFA editions, from FIFA 2017 to FIFA 2022. Each dataset contains detailed player attributes, including skills, physical attributes, potential ratings, wages, and market values. This structured data allows us to explore trends over time and predict players' financial worth based on their performance.")

    # Our Goal Section
    st.write("### Our Goal")
    st.write("Our main goal is to create an interactive and user-friendly application that provides valuable insights into FIFA player data. The app will allow users to:")
    st.write("- Preview raw data and explore different player attributes.")
    st.write("- Visualize player statistics and trends using interactive charts.")
    st.write("- Use a machine learning model to predict player salaries and market values.")
    st.write("By integrating data analytics and machine learning, we aim to make FIFA player analysis accessible to everyone, from casual gamers to data science enthusiasts.")

    # Final Message
    st.success("Let's dive into the world of FIFA data and uncover hidden insights together! ⚽")
