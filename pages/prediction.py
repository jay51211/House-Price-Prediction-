import streamlit as st
import numpy as np
import pickle
import os
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.title("🏡 Boston House Price Prediction")
st.markdown("Adjust the property features below to estimate house price.")
st.markdown("---")

c1, c2, c3, c4, c5 = st.columns([2, 1, 1, 1, 2])

with c2:
    if st.button("🏠 Home"):
        st.switch_page("app.py")

with c3:
    if st.button("📊 Predict"):
        st.switch_page("pages/prediction.py")

with c4:
    if st.button("📘 About"):
        st.switch_page("pages/about.py")

st.markdown("---")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, "model", "model.pkl")

with open(model_path, "rb") as f:
    model = pickle.load(f)

data_path = os.path.join(BASE_DIR, "HousingData.csv")
df = pd.read_csv(data_path)

left_col, right_col = st.columns(2)

with left_col:

    col1, col2, col3 = st.columns(3)

    with col1:
        with st.expander("🏙 Location & Environment", expanded=True):
            CRIM = st.number_input("Crime Rate (CRIM)", 0.0)
            ZN = st.number_input("Residential Land (ZN)", 0.0)
            INDUS = st.number_input("Non-Retail Business (INDUS)", 0.0)
            CHAS = st.selectbox("Charles River (CHAS)", [0, 1])

    with col2:
        with st.expander("🏠 Property Details", expanded=True):
            NOX = st.number_input("Nitric Oxide (NOX)", 0.0)
            RM = st.number_input("Rooms per Dwelling (RM)", 0.0)
            AGE = st.number_input("Age of Property (AGE)", 0.0)
            DIS = st.number_input("Distance to Employment (DIS)", 0.0)

    with col3:
        with st.expander("📊 Community Statistics", expanded=True):
            RAD = st.number_input("Accessibility to Highways (RAD)", 0)
            TAX = st.number_input("Property Tax (TAX)", 0)
            PTRATIO = st.number_input("Pupil-Teacher Ratio (PTRATIO)", 0.0)
            B = st.number_input("Proportion of Black Population (B)", 0.0)
            LSTAT = st.number_input("Lower Status Population % (LSTAT)", 0.0)

    st.markdown("---")
    predict = st.button("🔍 Predict Price")

fig = px.scatter(
    df,
    x="RM",
    y="MEDV",
    labels={"RM": "Average Rooms (RM)", "MEDV": "Median Value (MEDV)"},
    title="House Prices vs Number of Rooms"
)

if predict:

    features = np.array([[CRIM, ZN, INDUS, CHAS, NOX,
                          RM, AGE, DIS, RAD, TAX,
                          PTRATIO, B, LSTAT]])

    prediction = model.predict(features)

    st.success(f"💰 Estimated House Price: ${prediction[0]*1000:,.2f}")
    st.info("Note: MEDV is in $1000s (as per Boston dataset)")

    fig.add_trace(
        go.Scatter(
            x=[RM],
            y=[prediction[0]],
            mode="markers",
            marker=dict(size=18, symbol="x"),
            name="Predicted House"
        )
    )

fig.update_layout(
    height=600,
    title_x=0.3
)

with right_col:
    st.plotly_chart(fig, use_container_width=True)