from src.components.data_transformation import DataTransformation
import pandas as pd
from zenml import step

@step
def data_transformation_step(df: pd.DataFrame, features: list, target:str) -> pd.DataFrame:
    """
    Data transformation step
    """
    data_transformation = DataTransformation(df, features, target)
    return data_transformation.transform_data()