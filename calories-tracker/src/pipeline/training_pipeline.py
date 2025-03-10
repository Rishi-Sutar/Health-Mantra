from src.steps.data_ingestion_step import data_ingestion_step
from src.steps.clean_data_step import clean_data_step
from src.steps.data_spliter_step import data_spliter_step
from src.steps.data_transformation_step import data_transformation_step
from src.steps.model_selection_step import model_selection_step
from src.steps.model_trainer_step import model_trainer_step

import mlflow
from zenml import Model,pipeline
from zenml.client import Client
import os

mlflow.set_tracking_uri('http://localhost:5000')


@pipeline(
    model=Model(
        # The name uniquely identifies this model
        name="calories-tracker",
    ),
    enable_cache=False
)
def ml_pipeline():    
    
    with mlflow.start_run():

        path = os.path.join(os.getcwd(), "data", "calories.csv")
        data = data_ingestion_step(path)
        
        cleaned_data = clean_data_step(data, ["User_ID"])
        
        transformed_data = data_transformation_step(cleaned_data, ["Gender"], 'Calories')
        
        X_train, X_test, y_train, y_test = data_spliter_step(transformed_data, "Calories", 0.2)
        
        model_selection = model_selection_step(X_train, y_train)
        
        trained_model = model_trainer_step(model_selection, X_train, y_train)
    
        mlflow.sklearn.log_model(trained_model, "model")
        mlflow.log_params(model_selection["best_params"])
        mlflow.log_metric("best_score", model_selection["best_score"])

    
    
if __name__ == "__main__":
    ml_pipeline()