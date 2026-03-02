#  House Price Prediction (Machine Learning)

This repository contains a Jupyter Notebook project for **House Price Prediction** using Machine Learning regression models.  
The project focuses on **data preprocessing, handling missing values, outlier removal**, and training multiple regression models to predict house prices.

---

##  Project Overview

The notebook uses a housing dataset (`HousingData.csv`) and predicts the target variable:

 **MEDV** → Median value of owner-occupied homes

The notebook implements and compares multiple regression algorithms to find the best-performing model.

---

##  Features of This Project

###  1. Data Loading
- Loads the dataset using `pandas.read_csv()`

###  2. Data Cleaning & Missing Value Handling
Missing values are handled using `SimpleImputer`:

- **Mean Imputation** for:
  - `CRIM`, `ZN`, `INDUS`, `AGE`, `LSTAT`

- **Most Frequent Imputation** for:
  - `CHAS`

###  3. Exploratory Data Analysis (EDA)
The notebook includes:
- Dataset shape & info
- Missing values check
- Statistical summary (`describe()`)
- Scatter plots (example: `MEDV` vs `CRIM`)

###  4. Outlier Detection & Removal
Outliers are detected in the `MEDV` column using the **IQR method**:
- Computes Q1, Q3, and IQR
- Removes values outside the range:
  - `lower = Q1 - 1.5 * IQR`
  - `upper = Q3 + 1.5 * IQR`

###  5. Model Training & Evaluation
The dataset is split into training and testing sets using `train_test_split`.

Models used:

 **Linear Regression (with Pipeline)**
- `StandardScaler`
- `LinearRegression`

 **Decision Tree Regressor**
- `DecisionTreeRegressor()`

 **Random Forest Regressor**
- `RandomForestRegressor()`

###  6. Evaluation Metrics
Models are evaluated using:

- Mean Squared Error (MSE)
- Mean Absolute Error (MAE)

 Final conclusion: **Random Forest performed the best** (lowest MAE & MSE).

---

##  Technologies / Libraries Used

- Python  
- Pandas  
- Matplotlib  
- Seaborn  
- Scikit-learn  

---




