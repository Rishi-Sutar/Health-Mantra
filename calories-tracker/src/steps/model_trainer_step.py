from src.components.model_trainer import ModelTrainer
import pandas as pd
from sklearn.base import RegressorMixin

from zenml import step

@step
def model_trainer_step(model: dict, X_train: pd.DataFrame, y_train: pd.Series) -> RegressorMixin:
    """
    Step to train the model
    """
    model_trainer = ModelTrainer(model, X_train, y_train)
    trained_model = model_trainer.train_model()
    
    return trained_model