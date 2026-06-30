
import joblib

model = joblib.load("models/nids_model.pkl")

print("=" * 50)
print("MODEL INFORMATION")
print("=" * 50)

print(type(model))

print("\nNumber of Features:")

print(model.n_features_in_)

print("\nFeature Names:")

print(model.feature_names_in_)