import joblib
import pandas as pd

class Detector:
    def __init__(self, model_path="models/nids_model.pkl"):
        self.model = joblib.load(model_path)
    def predict(self, features):
        df = pd.DataFrame([features])

        prediction = self.model.predict(df)

        return prediction[0]
        