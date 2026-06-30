from flow_manager import FlowManager
from feature_extractor import FeatureExtractor

manager = FlowManager()

manager.process_packet(
    "192.168.1.10",
    "8.8.8.8",
    55000,
    53,
    "UDP",
    120
)

manager.process_packet(
    "192.168.1.10",
    "8.8.8.8",
    55000,
    53,
    "UDP",
    80
)

extractor = FeatureExtractor()

for flow in manager.get_all_flows().values():

    features = extractor.extract(flow)

    print("\n========== FEATURE VECTOR ==========")

for key, value in features.items():
    print(f"{key:20}: {value}")

print("=" * 36)