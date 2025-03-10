from src.components.data_spliter import DataSplitter
from zenml import step
import pandas as pd
from typing import Tuple

@step
def data_spliter_step(df: pd.DataFrame, target: str, test_size: float) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """
    Data spliting step
    """

    data_spliter = DataSplitter(df, target, test_size)
    X_train, X_test, y_train, y_test = data_spliter.split_data()
    return X_train, X_test, y_train, y_test