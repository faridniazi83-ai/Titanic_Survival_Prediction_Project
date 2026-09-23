import pandas as pd
import joblib

# Load trained model
model = joblib.load("titanic_model.pkl")

# New passenger data
passenger = pd.DataFrame({
    "Pclass": [1],
    "Sex": [1],
    "Age": [25],
    "SibSp": [0],
    "Parch": [0],
    "Fare": [80],
    "Embarked": [0]
})

# Prediction
prediction = model.predict(passenger)

if prediction[0] == 1:
    print("Passenger is predicted to Survive")
else:
    print("Passenger is predicted Not to Survive")