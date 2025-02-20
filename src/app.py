import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sklearn  # pip install scikit-learn 

from PIL import Image
import codecs
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu  # pip install streamlit-menu




st.title("FIFA Data Lab - The Game")
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Explore", "About", "Remarks"])

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
if page == "Explore":
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
        
    elif selected == "03: Pred":
        st.markdown("### :violet[Data Prediction]")
        st.markdown("<p style='font-size:20px; color:white;'>Select a dataset</p>", unsafe_allow_html=True)
        dataset_option = st.selectbox("FIFA Version: ",list(datasets.keys()));


    
elif page == "About":
    st.title("About")
    st.write("This is a placeholder for the About page. You can add more details about the app here.")
    
elif page == "Remarks":
    st.title("Remarks")
    st.write("This is a placeholder for the Remarks page. You can add conclusions or insights here.")

