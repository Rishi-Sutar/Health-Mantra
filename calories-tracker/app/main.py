from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
import os
import logging

# Setup logging configuration
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

app = FastAPI()

# Load the saved model, scalers, and label encoder
model_path = "artifacts/trained_model.joblib"
feature_scaler_path = "artifacts/feature_scaler.joblib"
target_scaler_path = "artifacts/target_scaler.joblib"
encoder_path = "artifacts/label_encoders.joblib"

if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file not found at {model_path}")

if not os.path.exists(feature_scaler_path):
    raise FileNotFoundError(f"Feature scaler file not found at {feature_scaler_path}")

if not os.path.exists(target_scaler_path):
    raise FileNotFoundError(f"Target scaler file not found at {target_scaler_path}")

if not os.path.exists(encoder_path):
    raise FileNotFoundError(f"Label encoder file not found at {encoder_path}")

model = joblib.load(model_path)
feature_scaler = joblib.load(feature_scaler_path)
target_scaler = joblib.load(target_scaler_path)
encoder = joblib.load(encoder_path)

class PredictionRequest(BaseModel):
    Gender: str
    Age: int
    Height: float
    Weight: float
    Duration: float
    Heart_Rate: float
    Body_Temp: float

@app.get("/features")
def get_features():
    try:
        # Get feature names (works for scikit-learn models)
        feature_names = list(model.feature_names_in_)
    except AttributeError:
        return {"error": "Feature names not found. The model might not store them."}

    return {"expected_features": feature_names}

@app.post("/predict")
def predict(request: PredictionRequest):
    try:
        # Convert the request data to a DataFrame
        data = pd.DataFrame([request.dict()])
        
        # Encode the 'Gender' column using the saved label encoder
        data['Gender'] = encoder['Gender'].transform(data['Gender'])
        
        # Ensure all expected columns are present
        expected_columns = ['Gender', 'Age', 'Height', 'Weight', 'Duration', 'Heart_Rate', 'Body_Temp']
        for col in expected_columns:
            if col not in data.columns:
                data[col] = 0
        
        # Reorder columns to match the training data
        data = data[expected_columns]
        
        # Scale the data using the saved feature scaler
        scaled_data = feature_scaler.transform(data)
        
        # Make predictions
        prediction = model.predict(scaled_data)
        
        # Inverse transform the prediction using the target scaler
        prediction = target_scaler.inverse_transform(prediction.reshape(-1, 1))
        
        return {"Calories": prediction[0][0]}
    
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)