import sys
import os
import streamlit as st

# Allow app to access src folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from src.features import prepare_features
from src.model import predict_burnout

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Employee Burnout Early Warning System",
    layout="wide"
)

# ---------------- HEADER ----------------
st.markdown("""
# 🧠 Employee Burnout Early-Warning System  
### AI-powered decision support tool for HR teams

This system predicts **burnout risk before attrition or performance decline**  
using **objective work and behavioral indicators**.
""")

st.divider()

# ---------------- LAYOUT ----------------
left_col, right_col = st.columns([1.2, 1])

# ================= LEFT PANEL =================
with left_col:
    st.subheader("👤 Employee Work Profile")

    age = st.slider("Age", 18, 60, 30)
    overtime = st.selectbox("Overtime Work", ["No", "Yes"])
    years_at_company = st.slider("Years at Company", 0, 40, 3)
    monthly_income = st.number_input("Monthly Income", min_value=1000, max_value=50000, value=5000)

    st.subheader("⚖️ Work & Satisfaction Indicators")

    work_life_balance = st.slider("Work-Life Balance (1 = Poor, 4 = Excellent)", 1, 4, 2)
    job_satisfaction = st.slider("Job Satisfaction (1 = Low, 4 = High)", 1, 4, 2)
    environment_satisfaction = st.slider("Environment Satisfaction (1 = Low, 4 = High)", 1, 4, 2)
    performance_rating = st.slider("Performance Rating", 1, 4, 3)
    attrition = st.selectbox("Past Attrition Indicator", ["No", "Yes"])

# ================= RIGHT PANEL =================
with right_col:
    st.subheader("📊 Burnout Risk Assessment")

    st.markdown("""
    This AI model evaluates:
    - Workload pressure  
    - Work-life imbalance  
    - Satisfaction signals  
    - Historical attrition patterns  
    """)

    # Prepare input
    input_df = prepare_features(
        age=age,
        overtime=overtime,
        work_life_balance=work_life_balance,
        job_satisfaction=job_satisfaction,
        environment_satisfaction=environment_satisfaction,
        monthly_income=monthly_income,
        years_at_company=years_at_company,
        performance_rating=performance_rating,
        attrition=attrition
    )

    if st.button("🔍 Predict Burnout Risk", use_container_width=True):
        result = predict_burnout(input_df)

        st.divider()

        if result == "High":
            st.error("🚨 **HIGH BURNOUT RISK**")
            st.markdown("""
            **Recommended HR Actions:**
            - Immediate workload review  
            - One-to-one discussion  
            - Mental health & flexibility support  
            """)
        elif result == "Medium":
            st.warning("⚠️ **MEDIUM BURNOUT RISK**")
            st.markdown("""
            **Recommended HR Actions:**
            - Monitor workload trends  
            - Encourage time-off  
            - Regular check-ins  
            """)
        else:
            st.success("✅ **LOW BURNOUT RISK**")
            st.markdown("""
            **Status:**
            - Healthy work conditions  
            - Continue positive practices  
            """)

# ---------------- FOOTER ----------------
st.divider()
st.caption(
    "⚠️ This system is a **decision-support tool**, not a medical diagnosis. "
    "Predictions are based on historical patterns and objective HR data."
)
