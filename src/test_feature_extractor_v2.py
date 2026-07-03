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

flow.add_packet(120)
time.sleep(1)      # Wait 1 second
flow.add_packet(80)
time.sleep(2)      # Wait 2 seconds

flow.add_packet(200)


extractor = FeatureExtractor()

features = extractor.extract(flow.to_dict())

print("\n========== FEATURE VECTOR ==========\n")

for key, value in features.items():
    print(f"{key:<35}: {value}")

print("\n====================================")