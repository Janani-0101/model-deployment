from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

app = FastAPI(title="Titanic Survival Prediction API")

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

class Passenger(BaseModel):
    Pclass: int
    Age: float
    SibSp: int
    Parch: int
    Fare: float
    Sex_male: int
    Embarked_Q: int
    Embarked_S: int

@app.get("/")
def home():
    return {"message": "Titanic Survival API is running"}

@app.post("/predict")
def predict_survival(data: Passenger):
    features = np.array([[
        data.Pclass,
        data.Age,
        data.SibSp,
        data.Parch,
        data.Fare,
        data.Sex_male,
        data.Embarked_Q,
        data.Embarked_S
    ]])

    prediction = model.predict(features)[0]

    return {
        "survived": bool(prediction)
    }
