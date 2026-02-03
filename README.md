# 🧠 Employee Burnout Early-Warning System (AI-Based)

An **AI-powered employee burnout prediction system** designed to identify burnout risk **before attrition or performance decline**, enabling proactive HR intervention.

This project leverages **machine learning (XGBoost)** and custom feature engineering on objective HR data to support intelligent, data-driven decision-making.

---

## 🚀 Problem Statement

Employee burnout is a critical challenge in modern organizations, impacting employee well-being, productivity, and retention.

Most existing burnout detection systems are:

- Reactive instead of predictive  
- Heavily dependent on employee surveys  
- Based on simple rule-based or linear models  
- Unable to capture complex behavioral patterns  

There is a need for an **AI-driven, predictive, and scalable solution** that can detect burnout early using objective indicators.

---

## 🎯 Project Objectives

- Predict employee burnout risk **before attrition occurs**
- Reduce bias by using **objective work-related indicators**
- Engineer a **custom burnout risk label**
- Apply an **optimized machine learning algorithm**
- Provide an **HR-friendly, interpretable dashboard**

---

## 🧩 Key Features

- 🔍 Predicts **Burnout Risk** (Low / Medium / High)
- 🧠 Custom-engineered burnout risk feature
- 📊 Exploratory Data Analysis (EDA)
- 🤖 Optimized **XGBoost** model for prediction
- 📦 Modular and reusable ML architecture

---

## 🧠 Burnout Risk Feature Engineering (Novelty)

Burnout is not directly available as a label in HR datasets.

This project introduces a **custom Burnout_Risk label** engineered using weighted objective indicators:

- Overtime workload  
- Work-life balance  
- Job satisfaction  
- Environment satisfaction  
- Attrition as a delayed burnout proxy  

This enables **early-warning burnout detection**, rather than post-event analysis.

---

## 🤖 Algorithms Used

| Algorithm | Purpose |
|------------|----------|
| Logistic Regression | Baseline model |
| Random Forest | Ensemble comparison |
| **XGBoost** | **Final optimized model** |

📌 XGBoost was selected due to its ability to capture **non-linear relationships**, handle structured HR data efficiently, and outperform traditional models.

---

## 🏗️ Project Structure

```text
employee_burnout_detection/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda.ipynb
│   └── 04_modeling.ipynb
│
├── src/
│   ├── preprocessing.py
│   ├── features.py
│   └── model.py
│
├── models/
│   ├── burnout_xgboost_model.pkl
│   └── burnout_label_encoder.pkl
│
├── app/
│   └── app.py
│
├── requirements.txt
├── README.md
└── .gitignore

```

🌐 Deployment (Streamlit Application)
The trained XGBoost model is deployed using Streamlit, providing:

Interactive user interface

Clean prediction layout

HR-friendly explanations

Actionable recommendations

▶️ Run the application locally:
streamlit run app/app.py
📊 Results & Insights
XGBoost achieved the best performance compared to baseline models.

Burnout risk shows strong correlation with:

Overtime

Poor work-life balance

Low satisfaction metrics

The system successfully identifies early burnout signals.

👩‍💻 Author
Monal Sree P
AI & Data Science Student