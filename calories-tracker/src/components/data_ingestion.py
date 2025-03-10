import pandas as pd
import numpy as np
import os
import logging
from dataclasses import dataclass

# Setup logging configuration
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

@dataclass
class DataIngestion:
    """
    Class to ingest data from CSV files
    """
    def __init__(self, path: str) -> pd.DataFrame:
        self.path = path

    def read_csv(self):
        """
        Read CSV file
        """
        try:
            df = pd.read_csv(self.path)
            data = df.copy()
            logging.info(f"Data read from {self.path}")
            return data
        except FileNotFoundError as e:
            logging.error(f"File not found: {e}")
            return None

if __name__ == "__main__":
    
    # Path to CSV file
    # path = os.path.join(os.getcwd(), "data", "calories.csv")
    # print(path)
    # data_ingestion = DataIngestion(path)
    # df = data_ingestion.read_csv()
    # print(df.head())
    pass