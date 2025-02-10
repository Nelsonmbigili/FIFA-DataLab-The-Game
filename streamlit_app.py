import streamlit as st
import pandas as pd

# App Title
st.title("Fifa Data Lab - The Game")
st.image("fifa_logo_image.png")
st.write("Welcome, it's great to have you!")

# Sidebar Menu
st.sidebar.title("Menu")

# List of dataset file paths
data_files = [
    "Datasets/FIFA17_official_data.csv",
    "Datasets/FIFA18_official_data.csv",
    "Datasets/FIFA19_official_data.csv",
    "Datasets/FIFA20_official_data.csv",
    "Datasets/FIFA21_official_data.csv",
    "Datasets/FIFA22_official_data.csv",
    "Datasets/FIFA23_official_data.csv"
]

# Dropdown selection for datasets
selected_file = st.sidebar.selectbox("Select a dataset", data_files)

# Load selected dataset
df = pd.read_csv(selected_file)
st.subheader(f"{selected_file} Preview")
st.dataframe(df.head())
