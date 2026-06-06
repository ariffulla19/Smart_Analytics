import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Smart Analytics Tool", layout="wide")

st.title("📊 Smart Analytics Tool")

uploaded_file = st.file_uploader(
    "Upload a CSV File",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.header("Dataset Preview")
    st.dataframe(df.head())

    st.header("Missing Value Analysis")
    st.write(df.isnull().sum())

    st.header("Statistical Summary")
    st.write(df.describe())

    numeric_cols = df.select_dtypes(include="number").columns

    if len(numeric_cols) > 0:

        st.header("Histogram")
        col = st.selectbox("Select Column", numeric_cols)
        fig1 = px.histogram(df, x=col)
        st.plotly_chart(fig1)

        st.header("Bar Chart")
        fig2 = px.bar(df.head(20), x=df.index[:20], y=col)
        st.plotly_chart(fig2)

        st.header("Scatter Plot")
        x_col = st.selectbox("X Axis", numeric_cols, key="x")
        y_col = st.selectbox("Y Axis", numeric_cols, key="y")
        fig3 = px.scatter(df, x=x_col, y=y_col)
        st.plotly_chart(fig3)

else:
    st.info("Please upload a CSV file.")