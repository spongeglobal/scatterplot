import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title
st.title("Scatter Plot Visualizer with Covariance and Correlation")

# Upload CSV file
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    # Read the data
    df = pd.read_csv(uploaded_file)
    st.write("Preview of dataset:")
    st.dataframe(df.head())

    # Select numeric columns
    numeric_cols = df.select_dtypes(include='number').columns.tolist()

    if len(numeric_cols) < 2:
        st.warning("Need at least two numerical columns to plot scatter plot.")
    else:
        # Column selectors
        x_axis = st.selectbox("Select X-axis", numeric_cols)
        y_axis = st.selectbox("Select Y-axis", numeric_cols, index=1 if len(numeric_cols) > 1 else 0)

        # Compute Covariance and Correlation
        covariance = df[[x_axis, y_axis]].cov().iloc[0, 1]
        correlation = df[[x_axis, y_axis]].corr().iloc[0, 1]

        # Display statistics
        st.markdown("### Covariance and Correlation")
        st.write(f"**Covariance ({x_axis}, {y_axis})**: {covariance:.4f}")
        st.write(f"**Correlation Coefficient ({x_axis}, {y_axis})**: {correlation:.4f}")

        # Plot
        fig, ax = plt.subplots()
        sns.scatterplot(data=df, x=x_axis, y=y_axis, ax=ax)
        ax.set_title(f"Scatter Plot: {x_axis} vs {y_axis}")
        st.pyplot(fig)
