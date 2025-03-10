import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
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
    st.markdown("## :blue[Data Overview]")
    st.markdown("### :violet[Select a dataset]")
    dataset_option = st.selectbox("FIFA Version: ",list(datasets.keys()));
    df = pd.read_csv(datasets[dataset_option])
    st.markdown("### :violet[Numerical Data Description]")
    st.dataframe(df.describe())
    st.markdown("### :violet[Non Numerical Data]")
    st.code('''
        "Name",
        "Nationality",
        "Club",
        "Preferred Foot",
        "Contract Valid Until"
        ''')
    st.markdown("### :violet[Data Preview Top 10 rows]")
    st.dataframe(df.head(10))
    # Select category to sort players
    st.markdown("### :violet[ View Top 10 Players Various Categories]")
    categories = [
        "Age", "Overall", "Potential", "Value(€M)", "Wage(€K)", "Height(Feet)", "Weight(Pounds)", "Acceleration", "SprintSpeed", "Agility", "Balance", "Strength", "Stamina", "Jumping",  
        "Crossing", "Finishing", "Dribbling", "FKAccuracy", "LongPassing", "BallControl", "Positioning", "Vision", "Composure",  
        "StandingTackle", "SlidingTackle", "Interceptions", "Aggression", 
        "GKDiving", "GKHandling", "GKKicking", "GKPositioning", "GKReflexes"  
    ]
    category = st.selectbox("Top Ten in:", categories)
## To be Modified
    if category in df.columns:
    # Base columns to display
        base_columns = ["Name","Nationality","Club", "Age", "Overall", "Value(€M)", "Wage(€K)"]
    
    # Add the selected category only if it's not already in base_columns
        columns_to_display = base_columns if category in base_columns else base_columns + [category]
    
    # Get top 10 players sorted by the selected category
        top_10_players = df.sort_values(by=category, ascending=False).head(10)
    
    # Display selected columns
        st.dataframe(top_10_players[columns_to_display])
    else:
        st.write("⚠️ Selected category not found in the dataset.")

    st.markdown("### :violet[Filter by: Player's Name, Nationality, or Club]")

    # Text input for player name
    player_name = st.text_input("Enter Player Name:", "")

    # Text input for nationality
    nationality = st.text_input("Enter Nationality:", "")

    # Text input for club
    club_name = st.text_input("Enter Club Name:", "")

    # Filtering data based on player name, nationality, or club
    filtered_data = df

    if player_name:
        filtered_data = filtered_data[filtered_data["Name"].str.contains(player_name, case=False, na=False)]

    if nationality:
        filtered_data = filtered_data[filtered_data["Nationality"].str.contains(nationality, case=False, na=False)]

    if club_name:
        filtered_data = filtered_data[filtered_data["Club"].str.contains(club_name, case=False, na=False)]

    # Display filtered data
    if not filtered_data.empty:
        st.dataframe(filtered_data)
    else:
        st.write("⚠️ No data found based on the search criteria.")
    
elif selected == "02: Viz":
    st.markdown("## :blue[Data Visualization]")
    st.markdown("### :violet[Select a dataset]")
    dataset_option = st.selectbox("FIFA Version: ",list(datasets.keys()));
    df = pd.read_csv(datasets[dataset_option])

    # Select only numeric columns
    Numeric_df = df.select_dtypes(include=['number'])

    # Define the expected columns
    expected_columns = ["Age", "Wage(€K)","Value(€M)", "Crossing", "Finishing", "Dribbling", 
                        "Acceleration", "Agility", "Strength", "Penalties", "Best Overall Rating"]
    
    Numeric_df.columns = Numeric_df.columns.str.strip()

    # Check for missing columns
    missing_columns = [col for col in expected_columns if col not in Numeric_df.columns]
    if missing_columns:
        st.warning(f"Missing columns: {missing_columns}")
    else:
        # Select only the required columns
        Filtered_Numeric_df = Numeric_df[expected_columns]

        st.markdown("##  Distributions of Football Players 📊")
        st.write("select a category to view Football Players Distibution")

        categories = {
            "Age": "Age",
            "Wage (€K)": "Wage(€K)",
            "Value(€M)": "Value(€M)",
            "Weight(Pounds)": "Weight(Pounds)",
            "Height(Feet)": "Height(Feet)",
            "Preferred Foot": "Preferred Foot",
            "Best Overall Rating": "Best Overall Rating"
        }

        bins = {
            "Age": [15, 20, 25, 30, 35, 40, 45],
            "Wage (€K)": [0, 50, 100, 200, 500, 1000, 5000],
            "Weight(Pounds)": [120, 140, 160, 180, 200, 220, 250],
            "Best Overall Rating": [40, 50, 60, 70, 80, 90, 100],
            "Value(€M)": [0, 0.28, 0.65, 1.5, 4.65, 10, 106],
            "Height(Feet)": [5.1, 5.11, 5.9, 6.1, 6.5, 6.9],
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
        # Sort sizes and labels by interval (left bound) for consistent ordering
        sorted_intervals = sorted(sizes.index, key=lambda x: x.left)
        sorted_sizes = sizes.loc[sorted_intervals]

        # Calculate percentages based on sorted sizes
        total = sorted_sizes.sum()
        percentages = (sorted_sizes / total) * 100

        # Plot pie chart (wedges in correct order)
        wedges, texts, autotexts = ax.pie(
            sorted_sizes,
            startangle=90,
            colors=sns.color_palette("Set2", n_colors=len(sorted_sizes)),  # Ensure color count matches
            wedgeprops={'edgecolor': 'black'},
            labels=None,
            autopct=lambda p: f'{p:.2f}%' if p > 3 else "",  # Hide very small values
            pctdistance=0.6
        )

        # Prepare formatted legend labels
        legend_labels = [f"{str(interval)} ({percentages[interval]:.2f}%)" for interval in sorted_intervals]

        # Create legend linked directly to wedges (color matches)
        ax.legend(
            wedges,  # Correct color order
            legend_labels,
            title=selected_category,
            loc="center left",
            bbox_to_anchor=(1, 0.5)
        )

        # Set title and label
        ax.set_ylabel("")
        ax.set_title(f"Distribution of {selected_category}")

        # Show plot
        st.pyplot(fig)

    else:
        # Bar Chart
        sns.barplot(x=sizes.index.astype(str), y=sizes.values, ax=ax, palette="Set2", edgecolor="black", order=sizes.index.sort_values()); ax.set_ylabel(""); ax.set_title(f"Distribution of {selected_category}"); ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right'); ax.yaxis.grid(True); ax.set_axisbelow(True)
        ax.set_ylabel("")
        ax.set_title(f"Distribution of {selected_category}")
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
        st.pyplot(fig)
    
    st.markdown("## Visualize Against Player Wage And Value 📊")
    # Select the metric (Value or Salary)
    metric = st.selectbox("Select Primary Attribute", ["Value(€M)", "Wage(€K)"],key="metric_selectbox")

    # Select the attribute for comparison
    categories = [
        "Overall","Potential", "Finishing","BallControl", "Crossing", "Dribbling", 
        "Acceleration", "Strength", "Stamina", "Aggression", "Positioning", 
        "Vision", "Composure", "GKDiving", "GKHandling"
    ]
    category = st.selectbox("Select Attribute to Relate", categories,key="category_selectbox")

    # Convert the "Value" and "Wage" columns to numeric
    df["Value(€M)"] = pd.to_numeric(df["Value(€M)"], errors='coerce')
    df["Wage(€K)"] = pd.to_numeric(df["Wage(€K)"], errors='coerce')
    
    # Handle missing values
    df = df.dropna(subset=[metric, category])

    # Visualize using a scatter plot
    if metric == "Value(€M)" and category in df.columns:
        # Scatter plot for Value vs the selected Category
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.scatterplot(x=df[category], y=df[metric], ax=ax, alpha=0.5, color='blue')
        ax.set_title(f'{category} vs {metric}')
        ax.set_xlabel(category)
        ax.set_ylabel(metric)
        st.pyplot(fig)

    elif metric == "Wage(€K)" and category in df.columns:
        # Scatter plot for Wage vs the selected Category
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.scatterplot(x=df[category], y=df[metric], ax=ax, alpha=0.5, color='green')
        ax.set_title(f'{category} vs {metric}')
        ax.set_xlabel(category)
        ax.set_ylabel(metric)
        st.pyplot(fig)

    st.markdown("## Visualize in Club or Nationality 📊")
    categories = ["Nationality", "Club"]
    category = st.selectbox("Select Category to Filter By", categories, key="filter")
    if category == "Club":
        category_value = st.text_input(f"Enter {category} to Filter", "Real Madrid")
    elif category == "Nationality":
        category_value = st.text_input(f"Enter {category} to Filter", "France")

    # Filter the data based on user input
    show_button = st.button("Show/Hide Violin Plots")
    if show_button:
        if category_value:
            filtered_df = df[df[category].str.contains(category_value, case=False, na=False)]
            if not filtered_df.empty:
                # Violin plot for Value(€M)
                fig, ax = plt.subplots(figsize=(8, 6))
                sns.violinplot(x=filtered_df[category], y=filtered_df["Value(€M)"], ax=ax, inner="point", color="pink")
                ax.set_title(f"Violin Plot of Value(€M) for {category_value} Players")
                ax.set_xlabel(category)
                ax.set_ylabel("Value(€M)")

                # Highlight the mean value on the violin plot
                mean_value = filtered_df["Value(€M)"].mean()
                ax.axhline(mean_value, color='red', linestyle='--', label=f'Mean Value: {mean_value:.2f}M')
                ax.legend()

                st.pyplot(fig)
                # Violin plot for Wage(€K)
                fig, ax = plt.subplots(figsize=(8, 6))
                sns.violinplot(x=filtered_df[category], y=filtered_df["Wage(€K)"], ax=ax, inner="point", color="lightgreen")
                ax.set_title(f"Violin Plot of Wage(€K) for {category_value} Players")
                ax.set_xlabel(category)
                ax.set_ylabel("Wage(€K)")

                # Highlight the mean wage on the violin plot
                mean_wage = filtered_df["Wage(€K)"].mean()
                ax.axhline(mean_wage, color='red', linestyle='--', label=f'Mean Wage: {mean_wage:.2f}K')
                ax.legend()

                st.pyplot(fig)
        else:
            st.write("⚠️ No data found for the selected filter.")
    
    # Compute correlation matrix
    correlation_matrix = Filtered_Numeric_df.corr()
    # Display heatmap
    st.markdown("## Heatmap of Feature Correlations 📊")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
    st.pyplot(fig)

elif selected == "03: Pred":
    st.markdown("## :blue[Data Prediction]")
    st.markdown("### :violet[Select a dataset]")
    dataset_option = st.selectbox("FIFA Version: ",list(datasets.keys()));
    df = pd.read_csv(datasets[dataset_option])

    st.markdown("##  Linear Regression 💶 ")
    # Option to select prediction type (Wage or Value)
    prediction_type = st.selectbox("Select Prediction Type", ("Wage", "Value"))

    if prediction_type == "Wage":
        st.markdown("## Predict Football Player's Wages 💶 ")

        features = st.multiselect(
            "Choose Features to use for Wages Prediction", 
            ["Age", "Value(€M)", "Overall", "Potential", "Acceleration", "SprintSpeed", 
            "Strength", "Stamina", "Finishing", "Dribbling", "BallControl", "Best Overall Rating"]
        )
        df = df.dropna(subset=features + ['Wage(€K)'])
        if st.button("Predict Wages") and features:
            X = df[features]
            y = df['Wage(€K)']

            # Split data
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

            # Train model
            model = LinearRegression()
            model.fit(X_train, y_train)

            # Predict and evaluate
            y_pred = model.predict(X_test)

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("Mean Absolute Error", 
                        f"€{metrics.mean_absolute_error(y_test, y_pred):.2f}K")

            with col2:
                st.metric("Mean Squared Error", 
                        f"€{metrics.mean_squared_error(y_test, y_pred):.2f}K")

            with col3:
                st.metric("R² Score", 
                        f"{metrics.r2_score(y_test, y_pred):.2f}")

            # Feature importance
            importance = pd.DataFrame({
                'feature': features,
                'importance': np.abs(model.coef_)
            }).sort_values('importance', ascending=False)

            st.markdown("### :violet[Feature Importance]")
            st.dataframe(importance)

            # Visualization: Actual vs Predicted Wages
            sns.scatterplot(x=y_test, y=y_pred, alpha=0.5)
            plt.xlabel("Actual Player Salary")
            plt.ylabel("Predicted Player Salary")
            plt.title("Actual vs Predicted Player Salary")
            st.pyplot(plt)

    elif prediction_type == "Value":
        st.markdown("## Predict Football Player's Value 💰 ")

        features = st.multiselect(
            "Choose Features to use for Value Prediction", 
            ["Age", "Wage(€K)", "Overall", "Potential", "Acceleration", "SprintSpeed", 
            "Strength", "Stamina", "Finishing", "Dribbling", "BallControl", "Best Overall Rating"]
        )
        df = df.dropna(subset=features + ['Value(€M)'])
        if st.button("Predict Value") and features:
            X = df[features]
            y = df['Value(€M)']

            # Split data
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

            # Train model
            model = LinearRegression()
            model.fit(X_train, y_train)

            # Predict and evaluate
            y_pred = model.predict(X_test)

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("Mean Absolute Error", 
                        f"€{metrics.mean_absolute_error(y_test, y_pred):.2f}M")

            with col2:
                st.metric("Mean Squared Error", 
                        f"€{metrics.mean_squared_error(y_test, y_pred):.2f}M")

            with col3:
                st.metric("R² Score", 
                        f"{metrics.r2_score(y_test, y_pred):.2f}")

            # Feature importance
            importance = pd.DataFrame({
                'feature': features,
                'importance': np.abs(model.coef_)
            }).sort_values('importance', ascending=False)

            st.markdown("### :violet[Feature Importance]")
            st.dataframe(importance)

            # Visualization: Actual vs Predicted Value
            sns.scatterplot(x=y_test, y=y_pred, alpha=0.5)
            plt.xlabel("Actual Player Value")
            plt.ylabel("Predicted Player Value")
            plt.title("Actual vs Predicted Player Value")
            st.pyplot(plt)

            