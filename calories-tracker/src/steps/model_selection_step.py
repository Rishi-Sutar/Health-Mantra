from src.components.model_selection import ModelSelection
import pandas as pd
from zenml import step

@step
def model_selection_step(X_train: pd.DataFrame, y_train: pd.Series) -> dict:
    model_selection = ModelSelection(X_train, y_train)
    return model_selection.select_model()