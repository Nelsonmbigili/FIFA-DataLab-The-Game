import streamlit as st

st.title("⚽ FIFA Data Lab: The Game")


st.markdown(r"""
### 🔑 Key Insights and Findings

The **FIFA Datalab** app provides a deep analysis of player statistics from FIFA 17 to FIFA 22. By exploring this data, we can uncover trends in player market values, wages, and performance over the years. Using a linear regression model, we aimed to predict player salaries and market values. Although the model's accuracy is limited, it still reveals important patterns in the football world.  

Here are some key insights we discovered: 
             
- **Prediction Accuracy**: Our linear regression model struggles with accuracy, suggesting that player salaries and values depend on complex factors not fully captured in the dataset.
- **Rising Star Players**: Young players with high potential often have higher market values even if their wages are still low. This shows how future potential influences a player's value.  
- **Impact of Nationality and Club**: Players who belong to top clubs or national teams usually have higher wages and market values, reflecting their exposure and opportunities.  
  

---

### 🔍 Reflections and Future Improvements  

Although the linear regression model has low predictive accuracy, it still captures ome real-world patterns in player valuations. However, to improve predictions, future models need to account for more complex and non-linear factors, such as:  

- **League Status**: Players from elite leagues (like the Premier League, La Liga) typically have higher wages and market value due to more exposure and competition.  
- **Club Reputation**: Players from famous or successful clubs are valued higher because of the club's status and history.  
- **National Team Reputation**: Representing a strong national team can increase a player’s market value.  
- **Fan Base**: Players in clubs with large, global fan bases are more marketable, increasing their value.  

---

### ⚽ Additional Observations from the Dataset  

The dataset also highlights interesting football trends:  

- **Foot Preference**: The data suggest that the majority of Footbal players are right footed.  
- **Correlation of Physical Attributes**: Strength, speed, and stamina  and attributes like spped, aceleration often greatly correlate.  
- **Skill Importance Variation**: Different skills (like dribbling, passing) are valued differently depending on a player's position.  

---

### 🙏 Special Thanks  

A big thank you to **EA Sports FIFA** for creating such detailed and rich datasets that inspire millions of fans and data enthusiasts. We also appreciate the **open-source community** for tools like **Pandas, Scikit-learn, Seaborn, and Streamlit** that made this app possible. Finally, thanks to **football fans and data enthusiasts** who shared valuable feedback and ideas!  

""")

st.success("Hope you enjoyed using the App, Consider sharing it with Friends! ⚽")

