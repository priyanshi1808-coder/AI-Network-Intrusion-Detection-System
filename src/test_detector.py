from detector import Detector
detector = Detector()

features = {
    "packet_count": 5,
    "total_bytes": 800,
    "duration": 2.5,
    "avg_packet_size": 160,
    "flow_bytes_per_sec": 320,
    "flow_packets_per_sec": 2,
    "min_packet_size": 120,
    "max_packet_size": 200,
    "mean_packet_size": 160,
    "std_packet_size": 31.62
}
prediction = detector.predict(features)
print("Prediction :", prediction)