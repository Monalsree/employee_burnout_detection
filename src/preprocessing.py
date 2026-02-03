import pandas as pd

def preprocess_raw_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Preprocess raw HR data for burnout prediction.

    Steps performed:
    - Select relevant burnout-related features
    - Encode categorical variables
    - Ensure clean, model-ready format

    Parameters
    ----------
    df : pd.DataFrame
        Raw HR dataset

    Returns
    -------
    pd.DataFrame
        Cleaned and preprocessed DataFrame
    """

    selected_cols = [
        'Age',
        'OverTime',
        'WorkLifeBalance',
        'JobSatisfaction',
        'EnvironmentSatisfaction',
        'MonthlyIncome',
        'YearsAtCompany',
        'PerformanceRating',
        'Attrition'
    ]

    df = df[selected_cols].copy()

    # Encode categorical columns
    df['OverTime'] = df['OverTime'].map({'Yes': 1, 'No': 0})
    df['Attrition'] = df['Attrition'].map({'Yes': 1, 'No': 0})

    return df
