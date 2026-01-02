# Diabetes Health Indicator Prediction 🏥

### A Machine Learning Classification Project

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Scikit-Learn](https://img.shields.io/badge/Library-Scikit--Learn-orange)
![Status](https://img.shields.io/badge/Status-Completed-green)

## 📋 Project Overview
This project focuses on building a binary classification model to predict whether a patient has diabetes (or pre-diabetes) based on 21 distinct health indicators. The analysis utilizes the **BRFSS 2015** dataset, a balanced dataset containing 70,692 responses.

The primary objective is to develop a robust machine learning pipeline to compare multiple models and identify the most effective predictor for this medical diagnostic task.

## 📊 The Dataset
**Source:** Behavioral Risk Factor Surveillance System (BRFSS) 2015.
**Filename:** `diabetes_binary_5050split_health_indicators_BRFSS2015.csv`

The dataset is a clean, 50-50 balanced split between diabetic and non-diabetic respondents, ensuring unbiased model training.
* **Target Variable:** `Diabetes_binary` (0 = Healthy, 1 = Diabetic/Pre-diabetic)
* **Key Features:** BMI, High Blood Pressure, Cholesterol, Smoker Status, Physical Activity, Age, Education, Income, etc.

## 🛠️ Tech Stack
* **Python:** Core programming language.
* **Pandas & NumPy:** Data manipulation and numerical operations.
* **Matplotlib & Seaborn:** Data visualization and correlation heatmaps.
* **Scikit-Learn:** Machine learning pipelines, models, and evaluation metrics.

## ⚙️ Methodology
This project adheres to rigorous Data Science practices to prevent data leakage and ensure reproducibility:

1.  **Exploratory Data Analysis (EDA):** analyzing correlations and feature distributions.
2.  **Preprocessing Pipeline:**
    * **Imputation:** Handling missing values via Median strategy.
    * **Scaling:** Standardization using `StandardScaler` (essential for linear models).
3.  **Cross-Validation:** Utilizing `StratifiedKFold` (5 splits) to validate model stability.
4.  **Model Comparison:**
    * **Baseline:** Logistic Regression.
    * **Ensemble:** Random Forest Classifier.

## How to Run the Code

### Prerequisites
Ensure you have Python installed. It is recommended to use a virtual environment.

### Installation Steps
1.  **Clone the repository** (if applicable) or download the project files.
2.  **Install dependencies** using the requirements file:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Launch Jupyter Notebook:**
    ```bash
    jupyter notebook
    ```
4.  **Open the notebook file** (e.g., `Diabetes_Prediction.ipynb`) and execute the cells sequentially.

## Results
After rigorous testing and Cross-Validation, the models yielded the following results:

| Model | Accuracy | Recall | F1-Score |
|-------|----------|--------|----------|
| **Logistic Regression** | **~75%** | **~76%** | **~75%** |
| Random Forest | ~74% | ~77% | ~74% |

**Conclusion:**
**Logistic Regression** was selected as the winning model. Despite simpler architecture compared to Random Forest, it offered comparable accuracy and superior interpretability—a critical factor in medical diagnostics where understanding risk factors (coefficients) is essential.

## 📂 Project Structure