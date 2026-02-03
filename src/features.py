import pandas as pd

def prepare_features(
    age: int,
    overtime: str,
    work_life_balance: int,
    job_satisfaction: int,
    environment_satisfaction: int,
    monthly_income: int,
    years_at_company: int,
    performance_rating: int,
    attrition: str
) -> pd.DataFrame:
    """
    Prepare model-ready features from raw input values.

    This function ensures:
    - Correct feature order
    - Proper encoding of categorical variables
    - Consistency with training data

    Returns
    -------
    pd.DataFrame
        Single-row DataFrame ready for prediction
    """

    data = {
        "Age": age,
        "OverTime": 1 if overtime == "Yes" else 0,
        "WorkLifeBalance": work_life_balance,
        "JobSatisfaction": job_satisfaction,
        "EnvironmentSatisfaction": environment_satisfaction,
        "MonthlyIncome": monthly_income,
        "YearsAtCompany": years_at_company,
        "PerformanceRating": performance_rating,
        "Attrition": 1 if attrition == "Yes" else 0
    }

    return pd.DataFrame([data])
