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
st.title("⚽ FIFA Data Lab: The Game")

# Datasets dictionary
datasets = {
    "FIFA17": "Datasets/FIFA17_official_data.csv",
    "FIFA18": "Datasets/FIFA18_official_data.csv",
    "FIFA19": "Datasets/FIFA19_official_data.csv",
    "FIFA20": "Datasets/FIFA20_official_data.csv",
    "FIFA21": "Datasets/FIFA21_official_data.csv",
    "FIFA22": "Datasets/FIFA22_official_data.csv",
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
    df = pd.read_csv(datasets[dataset_option])


    # Select only numeric columns
    Numeric_df = df.select_dtypes(include=['number'])

    # Define the expected columns
    expected_columns = ["Age", "Wage(€K)", "Crossing", "Finishing", "Dribbling", 
                        "Acceleration", "Agility", "Strength", "Penalties", "Best Overall Rating"]
    
    Numeric_df.columns = Numeric_df.columns.str.strip()

    # Check for missing columns
    missing_columns = [col for col in expected_columns if col not in Numeric_df.columns]
    if missing_columns:
        st.warning(f"Missing columns: {missing_columns}")
    else:
        # Select only the required columns
        Filtered_Numeric_df = Numeric_df[expected_columns]

        # Compute correlation matrix
        correlation_matrix = Filtered_Numeric_df.corr()

        # Display heatmap
        st.markdown("## 🔥 Heatmap of Feature Correlations")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
        st.pyplot(fig)

        st.markdown("## 🔥 Distributions of Football Playes")
        st.write("select a category to view Football Players Distibution")

        categories = {
            "Age": "Age",
            "Wage (€K)": "Wage(€K)",
            "Weight (lbs)": "Weight(lbs)",
            "Preferred Foot": "Preferred Foot",
            "Best Overall Rating": "Best Overall Rating"
        }

        bins = {
            "Age": [15, 20, 25, 30, 35, 40, 45],
            "Wage (€K)": [0, 50, 100, 200, 500, 1000, 5000],
            "Weight (lbs)": [120, 140, 160, 180, 200, 220, 250],
            "Best Overall Rating": [40, 50, 60, 70, 80, 90, 100]
        }
        # Allow user to select a category
        selected_category = st.selectbox("Choose a category:", list(categories.keys()))

        # Allow user to choose Pie or Bar Chart
        chart_type = st.radio("Select Chart Type:", ["Pie Chart", "Bar Chart"])

        # Convert numeric values into bins if necessary
        if selected_category in bins:
            df[categories[selected_category]].fillna(df[categories[selected_category]].median(), inplace=True)
            df[selected_category] = pd.cut(df[categories[selected_category]], bins=bins[selected_category])

        # Plotting the distribution
        fig, ax = plt.subplots(figsize=(8, 6))
    sizes = df[selected_category].value_counts()
    if chart_type == "Pie Chart":
        # Pie Chart
        labels = sizes.index.astype(str)

        wedges, texts, autotexts = ax.pie(
            sizes,
            startangle=90,
            colors=sns.color_palette("Set2"),
            wedgeprops={'edgecolor': 'black'},
            labels=None, 
            autopct=lambda p: f'{p:.2f}%' if p > 3 else "",  # Hide very small values
            pctdistance=0.6
        )

        ax.legend(wedges, labels, title=selected_category, loc="center left", bbox_to_anchor=(1, 0.5))
        ax.set_ylabel("")
        ax.set_title(f"Distribution of {selected_category}")
    else:
        # Bar Chart
        sns.barplot(x=sizes.index.astype(str), y=sizes.values, ax=ax, palette="Set2", edgecolor="black")
        ax.set_ylabel("")
        ax.set_title(f"Distribution of {selected_category}")
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45)

    # Show Chart
    st.pyplot(fig)

    st.markdown("## 🔥 Distributions of Football Playes")
    

   
elif selected == "03: Pred":
    st.markdown("### :violet[Data Prediction]")
    st.markdown("<p style='font-size:20px; color:white;'>Select a dataset</p>", unsafe_allow_html=True)
    dataset_option = st.selectbox("FIFA Version: ",list(datasets.keys()));
        