from src.components.clean_data import CleanData
from zenml import step
import pandas as pd

@step
def clean_data_step(df: pd.DataFrame, features: list) -> pd.DataFrame:
    """
    Clean data
    """
    clean_data = CleanData(df, features)
    return clean_data.data_clean()