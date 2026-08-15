import joblib
import pandas as pd


class Predictor:
    """
    Loads the trained AI-NVDS model
    and predicts the class of a flow.
    """

    def __init__(self, model_path="models/nids_model.pkl"):

        self.model = joblib.load(model_path)

        # Label mapping
        self.labels = {
           0: "BENIGN",
           1: "DDoS"
        }

        print("[INFO] Model loaded successfully.")

    def predict(self, features):
        """
        Predict attack/benign from extracted features.

        Parameters:
            features (dict)

        Returns:
            prediction
        """

        from model_features import MODEL_FEATURES

        filtered_features = {}

        for feature in MODEL_FEATURES:
            filtered_features[feature] = features.get(feature, 0)

        df = pd.DataFrame([filtered_features])

        prediction = self.model.predict(df)

        prediction_id = int(prediction[0])
        return self.labels.get(prediction_id, "Unknown")
        
    def predict_proba(self, features):
        """
        Return prediction probabilities.
        """

        from model_features import MODEL_FEATURES

        filtered = {}

        for feature in MODEL_FEATURES:
            filtered[feature] = features.get(feature, 0)

        df = pd.DataFrame([filtered])

        probability = self.model.predict_proba(df)

        return probability[0]

        
    
    