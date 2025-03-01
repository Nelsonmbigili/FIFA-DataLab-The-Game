import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import sklearn  # pip install scikit-learn 

from PIL import Image
import codecs
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu  # pip install streamlit-menu

st.title("FIFA Data Lab - The Game")

# Datasets dictionary
datasets = {
    "FIFA17": "Datasets/FIFA17_official_data.csv",
    "FIFA18": "Datasets/FIFA18_official_data.csv",
    "FIFA19": "Datasets/FIFA19_official_data.csv",
    "FIFA20": "Datasets/FIFA20_official_data.csv",
    "FIFA21": "Datasets/FIFA21_official_data.csv",
    "FIFA22": "Datasets/FIFA22_official_data.csv",
    "FIFA23": "Datasets/FIFA23_official_data.csv",
}

st.title("Explore")
selected = option_menu(menu_title=None, options=["01: Data", "02: Viz", "03: Pred"], orientation="horizontal")

if selected == "01: Data":
    st.markdown("### :violet[Data Overview]")
    st.markdown("## :blue[Select a dataset]")
    dataset_option = st.selectbox("FIFA Version: ",list(datasets.keys()));
    df = pd.read_csv(datasets[dataset_option])
    st.title("Data Preview:")
    st.dataframe(df.describe())
    st.write("View Top 10 Players Various Categories ")
    category=st.selectbox("Top Ten in :", ["Age", "Overall", "Potential", "Special"])
        
elif selected == "02: Viz":
    st.markdown("### :violet[Data Visualization]")
    st.markdown("## :blue[Select a dataset]")
    dataset_option = st.selectbox("FIFA Version: ",list(datasets.keys()));
    df = datasets[dataset_option]

    st.subheader("Distribution of Player Ratings")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.histplot(df["Overall"], bins=20, kde=True, color="purple", ax=ax)
    ax.set_xlabel("Overall Rating")
    ax.set_ylabel("Count")
    st.pyplot(fig)

    #2. Age vs. Overall Rating
    st.subheader("Age vs. Overall Rating")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.scatterplot(x=df["Age"], y=df["Overall"], alpha=0.5, color="blue", ax=ax)
    ax.set_xlabel("Age")
    ax.set_ylabel("Overall Rating")
    st.pyplot(fig)

    # 3. Club-wise Average Player Rating
    st.subheader("Top 10 Clubs by Average Player Rating")
    top_clubs = df.groupby("Club")["Overall"].mean().nlargest(10)
    fig, ax = plt.subplots(figsize=(8, 5))
    top_clubs.sort_values().plot(kind="barh", color="green", ax=ax)
    ax.set_xlabel("Average Rating")
    ax.set_ylabel("Club")
    st.pyplot(fig)

    # 4. Preferred Foot Distribution
    st.subheader("Preferred Foot Distribution")
    fig, ax = plt.subplots(figsize=(6, 4))
    df["Preferred Foot"].value_counts().plot(kind="pie", autopct="%1.1f%%", colors=["gold", "cyan"], ax=ax)
    ax.set_ylabel("")  
    st.pyplot(fig)

    # 5. Value vs. Wage
    st.subheader("Player Value vs. Wage")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.scatterplot(x=df["Value"].str.replace("€", "").str.replace("M", "").astype(float), 
                    y=df["Wage"].str.replace("€", "").str.replace("K", "").astype(float), 
                    alpha=0.5, color="red", ax=ax)
    ax.set_xlabel("Value (Millions €)")
    ax.set_ylabel("Wage (Thousands €)")
    st.pyplot(fig)
elif selected == "03: Pred":
    st.markdown("### :violet[Data Prediction]")
    st.markdown("<p style='font-size:20px; color:white;'>Select a dataset</p>", unsafe_allow_html=True)
    dataset_option = st.selectbox("FIFA Version: ",list(datasets.keys()));
        