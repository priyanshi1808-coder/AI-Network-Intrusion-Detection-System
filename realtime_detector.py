import joblib
import pandas as pd
from datetime import datetime
import os

MODEL_PATH = "models/nids_model.pkl"

model = joblib.load(MODEL_PATH)

CSV_FILE = "logs/alerts.csv"

if not os.path.exists(CSV_FILE):

    pd.DataFrame(columns=[
        "Time",
        "Source IP",
        "Destination IP",
        "Protocol",
        "Prediction",
        "Confidence"
    ]).to_csv(CSV_FILE, index=False)
    
def save_alert(src_ip,
               dst_ip,
               protocol,
               prediction,
               confidence):

    row = {

        "Time": datetime.now(),

        "Source IP": src_ip,

        "Destination IP": dst_ip,

        "Protocol": protocol,

        "Prediction": prediction,

        "Confidence": f"{confidence:.2f}%"
    }

    pd.DataFrame([row]).to_csv(

        CSV_FILE,

        mode="a",

        header=False,

        index=False
    )