import csv
import os
from datetime import datetime


class AlertLogger:

    def __init__(self, logfile="logs/alerts.csv"):

        self.logfile = logfile

        os.makedirs("logs", exist_ok=True)

        if not os.path.exists(self.logfile):
            

            with open(self.logfile, "w", newline="") as file:

                writer = csv.writer(file)

                writer.writerow([
                    "Time",
                    "Source IP",
                    "Destination IP",
                    "Source Port",
                    "Destination Port",
                    "Protocol",
                    "Prediction",
                    "Confidence",
                    "Severity"
                ])

    def log(
        self,
        src_ip,
        dst_ip,
        src_port,
        dst_port,
        protocol,
        prediction,
        confidence
    ):
        # Determine threat severity

        if prediction == "BENIGN":
           severity = "Low"

        elif confidence >= 99:
           severity = "High"

        elif confidence >= 90:
            severity = "Medium"

        else:
            severity = "Low"

        with open(self.logfile, "a", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                src_ip,
                dst_ip,
                src_port,
                dst_port,
                protocol,
                prediction,
                f"{confidence:.2f}%",
                severity
                
            ])