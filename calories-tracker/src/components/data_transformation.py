import pandas as pd
import numpy as np
import os
import logging
from dataclasses import dataclass
import joblib

from sklearn.preprocessing import StandardScaler, LabelEncoder

# Setup logging configuration
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

@dataclass
class DataTransformation:
    def __init__(self, df: pd.DataFrame, categorical_features: list, target: str):
        self.df = df
        self.categorical_features = categorical_features
        self.target = target
    
    def transform_data(self) -> pd.DataFrame:
        """
        Function to transform data: Label encodes categorical features and standardizes numerical features.
        """
        try:
            df = self.df.copy()
            
            # Label encode categorical features
            le_dict = {}
            for feature in self.categorical_features:
                le = LabelEncoder()
                df[feature] = le.fit_transform(df[feature])
                le_dict[feature] = le
                logging.info(f"Label encoded {feature}")
            
            # Save the label encoders for future use
            encoder_filename = "artifacts/label_encoders.joblib"
            os.makedirs(os.path.dirname(encoder_filename), exist_ok=True)
            joblib.dump(le_dict, encoder_filename)
            logging.info(f"Label encoders saved to {encoder_filename}")
            
            # Standardize numerical features
            numerical_features = df.select_dtypes(include=[np.number]).columns.tolist()
            numerical_features = [col for col in numerical_features if col != self.target]
            
            feature_scaler = StandardScaler()
            df[numerical_features] = feature_scaler.fit_transform(df[numerical_features])
            logging.info(f"Standardized numerical features: {numerical_features}")
            
            # Save the feature scaler for future use
            feature_scaler_filename = "artifacts/feature_scaler.joblib"
            joblib.dump(feature_scaler, feature_scaler_filename)
            logging.info(f"Feature scaler saved to {feature_scaler_filename}")
            
            # Standardize the target column
            target_scaler = StandardScaler()
            df[self.target] = target_scaler.fit_transform(df[[self.target]])
            logging.info(f"Standardized target column: {self.target}")
            
            # Save the target scaler for future use
            target_scaler_filename = "artifacts/target_scaler.joblib"
            joblib.dump(target_scaler, target_scaler_filename)
            logging.info(f"Target scaler saved to {target_scaler_filename}")
            
            logging.info("Data transformation completed")
            return df
        
        except Exception as e:
            logging.error(f"Error: {e}")
            raise e