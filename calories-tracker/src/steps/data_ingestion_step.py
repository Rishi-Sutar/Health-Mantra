from src.components.data_ingestion import DataIngestion
import pandas as pd

from zenml import step
import os

@step 
def data_ingestion_step(path: str) -> pd.DataFrame:
    """
    Data ingestion step
    """

    data_ingestion = DataIngestion(path)
    df = data_ingestion.read_csv()
    return df