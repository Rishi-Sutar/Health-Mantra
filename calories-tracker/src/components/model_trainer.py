import pandas as pd 
import numpy as np
from dataclasses import dataclass
import logging
import os
import joblib

from sklearn.linear_model import Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import make_scorer, mean_squared_error
from sklearn.base import RegressorMixin

import warnings
warnings.filterwarnings("ignore")

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

@dataclass
class ModelTrainer:
    
    def __init__(self, model: dict, X_train: pd.DataFrame, y_train: pd.Series):
        self.model_name = model['best_model']
        self.params = model['best_params']
        self.X_train = X_train
        self.y_train = y_train
        
    def train_model(self) -> RegressorMixin:
        """
        Function to train the model
        """
        if self.model_name == "Ridge":
            model = Ridge(**self.params)
        elif self.model_name == "Lasso":
            model = Lasso(**self.params)
        elif self.model_name == "RandomForestRegressor":
            model = RandomForestRegressor(**self.params)
        elif self.model_name == "Decision Tree":
            model = DecisionTreeRegressor(**self.params)
        else:
            raise ValueError(f"Model {self.model_name} not found")
        
        model.fit(self.X_train, self.y_train)
        
        model_filename = f"artifacts/trained_model.joblib"
        os.makedirs(os.path.dirname(model_filename), exist_ok=True)
        joblib.dump(model, model_filename)
        logging.info(f"Model saved to {model_filename}")
        
        logging.info(f"Model {self.model_name} trained successfully")
        
        
        
        return model