import streamlit as st

st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------- Custom CSS ----------
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }
    .title {
        font-size: 45px;
        font-weight: bold;
        color: #FFFFFF;
        text-align: center;
    }
    .subtitle {
        font-size: 22px;
        color: #FFFFFF;
        text-align: center;
    }
    .feature-box {
        background-color: black;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>🏠 House Price Prediction System</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Machine Learning Based Real Estate Price Estimator</div>", unsafe_allow_html=True)

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

col1, col2 = st.columns(2)

with col1:
    st.image("https://images.unsplash.com/photo-1560518883-ce09059eeffa", use_container_width=True)

with col2:
    st.markdown("""
    ### 📌 Project Overview

    This system predicts house prices using a **Random Forest Regression model**.

    It analyzes important property features such as:
    - 🏠 Area (Square Feet)
    - 🛏 Bedrooms
    - 🛁 Bathrooms
    - 🏢 Stories
    - 🚗 Parking Spaces

    ---

    🎯 **Goal:**  
    To demonstrate how Machine Learning can solve real-world real estate pricing problems.

    👉 Click on **Predict** to estimate a house price.
    """)

st.markdown("---")

f1, f2, f3 = st.columns(3)

with f1:
    st.markdown("""
    <div class='feature-box'>
    <h4>🤖 ML Powered</h4>
    <p>Uses Random Forest Regressor for accurate predictions.</p>
    </div>
    """, unsafe_allow_html=True)

with f2:
    st.markdown("""
    <div class='feature-box'>
    <h4>📊 Data Driven</h4>
    <p>Trained on real housing dataset with multiple features.</p>
    </div>
    """, unsafe_allow_html=True)

with f3:
    st.markdown("""
    <div class='feature-box'>
    <h4>⚡ Fast Prediction</h4>
    <p>Instant price estimation with user-friendly interface.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.success("Built using Python • Scikit-learn • Streamlit")