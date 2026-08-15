import joblib

model = joblib.load("models/nids_model.pkl")

print("Number of Features:", len(model.feature_names_in_))

print("\nModel Features:\n")

for f in model.feature_names_in_:
    print(f)