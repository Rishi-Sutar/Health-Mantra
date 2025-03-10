import pandas as pd 
import numpy as np
import os
import logging
from dataclasses import dataclass

from sklearn.model_selection import train_test_split

# Setup logging configuration
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

@dataclass
class DataSplitter:
    def __init__(self, df: pd.DataFrame, target: str, test_size: float = 0.2) -> pd.DataFrame:
        self.df = df
        self.target = target
        self.test_size = test_size

    def split_data(self) -> pd.DataFrame:
        """
        Function to split data into training and testing sets
        """
        try:
            X = self.df.drop([self.target], axis=1)
            y = self.df[self.target]
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=self.test_size, random_state=42)
            logging.info(f"Data split into training and testing sets")
            return X_train, X_test, y_train, y_test
        except Exception as e:
            logging.error(f"Error: {e}")
            raise e
        
if __name__ == "__main__":
    pass