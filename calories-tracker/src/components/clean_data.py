import pandas as pd
import numpy as np
import os
import logging

# Setup logging configuration
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


class CleanData:
    
    def __init__(self, df: pd.DataFrame, features: list):
        self.df = df
        self.features = features

    def data_clean(self) -> pd.DataFrame:
        """
        Function to clean data
        """
        try:
            # Drop rows with missing values
            df = self.df.copy()
            df = df.dropna()
            
            logging.info("Dropped rows with missing values")
            
            for feature in self.features:
                df.drop([feature], axis=1, inplace=True)
                logging.info(f"Dropped {feature}")
            
            num_cols = df.select_dtypes(include=[np.number]).columns
            
            for feature in num_cols:
                # Remove outliers
                q1 = df[feature].quantile(0.25)
                q3 = df[feature].quantile(0.75)
                iqr = q3 - q1
                lower_bound = q1 - 1.5 * iqr
                upper_bound = q3 + 1.5 * iqr
                df = df[(df[feature] > lower_bound) & (df[feature] < upper_bound)]
            
            logging.info(f"Removed outliers")
            return df   
        except Exception as e:
            logging.error(f"Error: {e}")
            raise e