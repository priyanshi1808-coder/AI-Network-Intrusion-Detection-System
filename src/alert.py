from datetime import datetime


class AlertManager:

    def __init__(self):
        self.alert_count = 0

    def raise_alert(self, flow, prediction, confidence):

        self.alert_count += 1

        print("\n")
        print("=" * 50)
        print("🚨 ATTACK DETECTED")
        print("=" * 50)

        print("Alert ID    :", self.alert_count)
        print("Time        :", datetime.now().strftime("%H:%M:%S"))
        print("Source IP   :", flow.src_ip)
        print("Destination :", flow.dst_ip)
        print("Protocol    :", flow.protocol)
        print("Prediction  :", prediction)
        print(f"Confidence  : {confidence:.2f}%")

        print("=" * 50)