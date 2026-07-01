from feature_extractor import FeatureExtractor

flow = {
    "packet_count": 5,
    "total_bytes": 800,
    "duration": 2.5,
    "packet_sizes": [120, 160, 180, 140, 200]
}

extractor = FeatureExtractor()

features = extractor.extract(flow)

print("\n========== FEATURE VECTOR ==========\n")

for key, value in features.items():
    print(f"{key:<25}: {value}")

print("\n====================================")