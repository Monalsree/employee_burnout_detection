import os
import joblib
import pandas as pd

# Get absolute path to project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Paths to saved model files
MODEL_PATH = os.path.join(BASE_DIR, "models", "burnout_xgboost_model.pkl")
ENCODER_PATH = os.path.join(BASE_DIR, "models", "burnout_label_encoder.pkl")

# Load trained model and label encoder
model = joblib.load(MODEL_PATH)
label_encoder = joblib.load(ENCODER_PATH)


def predict_burnout(input_df: pd.DataFrame) -> str:
    """
    Predict burnout risk for an employee.

    Parameters:
    ----------
    input_df : pd.DataFrame
        A DataFrame with the following columns:
        - Age
        - OverTime
        - WorkLifeBalance
        - JobSatisfaction
        - EnvironmentSatisfaction
        - MonthlyIncome
        - YearsAtCompany
        - PerformanceRating
        - Attrition

    Returns:
    -------
    str
        Burnout Risk Level: 'Low', 'Medium', or 'High'
    """

    prediction = model.predict(input_df)
    burnout_label = label_encoder.inverse_transform(prediction)[0]

    return burnout_label
