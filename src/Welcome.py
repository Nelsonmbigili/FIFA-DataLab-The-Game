import streamlit as st
from PIL import Image

# Display loading spinner
with st.spinner('Loading page...'):
    
    # Title and Welcome Message
    st.title("⚽ Fifa Data Lab: The Game")
    st.subheader(":violet[Welcome! We are glad to have you!]")
    
    # Display FIFA Logo
    image_path = Image.open("./Assets/fifa_logo.png")
    st.image(image_path)
    
    # App Navigation Guide
    st.write("### Navigating the App:")
    st.markdown("⚡ **Step into the game!** Use the legendary sidebar on the left to embark on your FIFA Data Lab journey!⚽")
    st.write(
        "- **Welcome Page:** Navigating the App & Meet the Team.\n"
        "- **About Page:** Motivation and Objectives.\n"
        "- **Explore Page:** Preview and Visualize Data & Linear Regression on Salaries of Football Players\n"
        "- **Remarks:** Conlusion and Insights from the Team.\n"
    )

     # Team Members Information
    st.write("### Meet the Team:")
    team_members = {
        "Ryan Opande": "rjo9414@nyu.edu",
        "Uditi Sharma": "us2133@nyu.edu",
        "Nelson Mbigili": "nfm8340@nyu.edu",
        "Dhruv Gopan": "dag10005@nyu.edu"
    }
    for name, email in team_members.items():
        st.write(f"- **{name}** ({email})")

    st.success("Enjoy exploring FIFA Data Lab!")
