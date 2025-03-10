import pandas as pd 
import numpy as np
from dataclasses import dataclass
import logging

from sklearn.model_selection import RandomizedSearchCV
from sklearn.linear_model import Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import make_scorer, mean_squared_error

import warnings
warnings.filterwarnings("ignore")

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

@dataclass
class ModelSelection:
    
    def __init__(self, X_train: pd.DataFrame, y_train: pd.Series):
        self.X_train = X_train
        self.y_train = y_train
    
    def select_model(self) -> dict:
        """
        Function to select the best model for the given data
        """
        # Define the models
        models = {
            "Ridge": {
                "model": Ridge(),
                "params": {
                    "alpha": [0.1, 1, 10]
                }
            },
            "Lasso": {
                "model": Lasso(),
                "params": {
                    "alpha": [0.1, 1, 10]
                }
            },
            "RandomForestRegressor": {
                "model": RandomForestRegressor(),
                "params": {
                    "n_estimators": [100, 200, 300],
                    "max_depth": [5, 10, 15]
                }
            },
            "Decision Tree": {
                "model": DecisionTreeRegressor(),
                "params": {
                    "max_depth": [5, 10, 15]
                }
            }
        }
        
        # Define the scoring function
        scoring = make_scorer(mean_squared_error, greater_is_better=False)
        
        best_score = float("inf")
        best_model = None
        best_params = None
        
        # Perform RandomizedSearchCV
        for model_name, model in models.items():
            logging.info(f"Training {model_name}")
            clf = RandomizedSearchCV(model["model"], model["params"], scoring=scoring)
            clf.fit(self.X_train, self.y_train)
            if clf.best_score_ < best_score:
                best_score = clf.best_score_
                best_model = model_name
                best_params = clf.best_params_
            logging.info(f"Best parameters for {model_name}: {clf.best_params_}")
        
        logging.info(f"Best model: {best_model}, Best score: {best_score}, Best parameters: {best_params}") 
        
        return {"best_model": best_model, "best_params": best_params}