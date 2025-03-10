import streamlit as st

st.title("⚽ FIFA Data Lab: The Game")


st.markdown(r"""
### Key Insights and Findings
The **FIFA Datalab** app offers a comprehensive look at player statistics across multiple FIFA versions. By leveraging data from FIFA 17 to FIFA 22, we were able to observe trends in player values, wages, and performance over the years. Using a simple linear Regression model, we successfully predict player salaries and market values with high accuracy, providing fans and data enthusiasts with unique insights into the game. Some key findings include:

- **Rising Star Players**: Younger players with high potential tend to have a lower wage but a significantly higher market value.
- **Impact of Nationality and Club**: Players from top-tier clubs or nations generally have higher wages and market values.
- **Prediction Accuracy**: Our linear regression model provided solid predictions, offering a realistic view of player salaries based on their in-game attributes.

### Reflections and Works for Future
Although the app provides accurate predictions, there’s always room for improvement and expansion. Future updates could include:
- **Incorporating more features**: Additional attributes like player injuries, playing styles, or historical performance could improve model accuracy.
- **Expanding datasets**: Including more recent versions of FIFA or adding external data sources like player transfers could further enhance the model's predictions.
- **Advanced Models**: Transitioning from linear regression to more complex models such as Random Forest or XGBoost could refine the accuracy of the predictions.

### Special Thanks
A big thank you to all the creators of FIFA for providing such detailed datasets and for inspiring millions worldwide. Additionally, thanks to the open-source community for the tools and libraries (like Pandas, Scikit-learn, Seaborn, and Streamlit) that made this app possible. Finally, we appreciate the FIFA fans and data enthusiasts who contributed valuable feedback.

""")

st.success("Hope you enjoyed using the App, Consider sharing it with Friends! ⚽")

