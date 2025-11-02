from fastapi import FastAPI
import joblib
import pandas as pd
import os

app = FastAPI()

# Get absolute path to model
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, "..", "models", "diabetes_model.pkl")

model = joblib.load(model_path)

@app.post("/predict")
def predict(data: dict):
    df = pd.DataFrame([data])
    prediction = model.predict(df)
    return {"prediction": int(prediction[0])}
