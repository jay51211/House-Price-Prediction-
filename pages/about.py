import streamlit as st

st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.title("📘 About This Project")

st.write("---")

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

st.markdown("""
## 🏠 House Price Prediction using Machine Learning

This project is based on the **Boston Housing Dataset**, a well-known dataset 
used in Machine Learning for regression problems.

The goal is to predict the **Median Value of Owner-Occupied Homes (MEDV)** 
in Boston suburbs.

---

### 🔍 Problem Statement

Real estate pricing is influenced by multiple factors such as:
- Area
- Number of Bedrooms
- Bathrooms
- Stories
- Parking Space

Accurate price prediction helps:
- Buyers make informed decisions
- Sellers price properties correctly
- Real estate agencies analyze market trends

---

## 📊 Dataset Information

The dataset contains **13 input features**:

1. **CRIM** – Crime rate per capita  
2. **ZN** – Residential land zoned for large lots  
3. **INDUS** – Non-retail business proportion  
4. **CHAS** – Charles River dummy variable (0 or 1)  
5. **NOX** – Nitric oxide concentration  
6. **RM** – Average number of rooms  
7. **AGE** – Proportion of old houses  
8. **DIS** – Distance to employment centers  
9. **RAD** – Accessibility to highways  
10. **TAX** – Property tax rate  
11. **PTRATIO** – Pupil-teacher ratio  
12. **B** – Proportion of Black population  
13. **LSTAT** – % lower status population  

### 🎯 Target Variable:
**MEDV** – Median value of homes (in $1000s)

---

### 🤖 Machine Learning Model Used

We used:

### 🌲 Random Forest Regressor

Why Random Forest?
- High accuracy
- Handles non-linearity well
- Reduces overfitting
- Works well on structured datasets

---

### 🛠️ Technologies Used

- Python
- Pandas & NumPy
- Scikit-learn
- Streamlit
- Matplotlib (for analysis)

---

### 📊 Model Performance

The model was trained on historical housing data and evaluated using regression metrics such as:
- R² Score
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)

---

### 🎓 Academic Purpose

This project demonstrates:
- Data preprocessing
- Model training
- Model saving/loading
- Deployment using Streamlit
- UI development for ML systems

---

### 🚀 Future Improvements

- Add more features (location, furnishing, etc.)
- Improve UI with advanced visualization
""")

st.success("Thank you for reviewing this project 🙌")