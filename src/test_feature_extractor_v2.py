import time

from flow import Flow
from feature_extractor import FeatureExtractor

flow = Flow(
    "192.168.1.10",
    "8.8.8.8",
    5000,
    443,
    "TCP"
)

flow.add_packet(120, header_length=20)

time.sleep(1)

flow.add_packet(80, header_length=20)

time.sleep(2)

flow.add_packet(200, header_length=20)

time.sleep(1)

flow.add_packet(
    150,
    direction="backward",
    header_length=20
)


extractor = FeatureExtractor()

features = extractor.extract(flow.to_dict())

print("\n========== FEATURE VECTOR ==========\n")

for key, value in features.items():
    print(f"{key:<35}: {value}")

print("\n====================================")
