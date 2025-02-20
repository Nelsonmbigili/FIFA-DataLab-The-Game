import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sklearn # pip install  scikit-learn 

from streamlit_option_menu import option_menu # type: ignore # pip install streamlit-menu
st.title("FIFA Data Lab - The Game")
selected = option_menu(menu_title=None,options=["01: Data","02: Viz","03: Pred",],orientation="horizontal")

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
if(selected=="01: Data"):
    st.markdown("### :violet[Data Overview]")
    st.expander("Show Code")
    

elif(selected=="02: Viz"):
    st.markdown("### :violet[Data Visualization]")


elif(selected=="03: Pred"):
    st.markdown("### :violet[Data Prediction]")





# App Title



