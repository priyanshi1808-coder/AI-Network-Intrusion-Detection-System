import time

from flow import Flow
from feature_extractor import FeatureExtractor
from predictor import Predictor


def main():

    print("=" * 50)
    print("AI-NVDS Prediction Test")
    print("=" * 50)

    # Create a sample flow
    flow = Flow(
        src_ip="192.168.1.10",
        dst_ip="142.250.183.14",
        src_port=50000,
        dst_port=443,
        protocol="TCP"
    )

    # Simulate packets
    flow.add_packet(100, "forward", header_length=20)
    time.sleep(1)

    flow.add_packet(200, "forward", header_length=20)
    time.sleep(2)

    flow.add_packet(150, "backward", header_length=20)
    time.sleep(1)

    flow.add_packet(100, "forward", header_length=20)

    # Convert Flow -> Dictionary
    flow_data = flow.to_dict()

    # Extract Features
    extractor = FeatureExtractor()
    features = extractor.extract(flow_data)

    print("\nExtracted Features:", len(features))

    # Load Predictor
    predictor = Predictor()

    # Predict
    prediction = predictor.predict(features)

    print("\nPrediction")
    print("-" * 30)
    print(prediction)

    print("\nDone!")


if __name__ == "__main__":
    main()