import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier
import joblib

# Load Dataset
df = pd.read_csv("data/cicids.csv")

# Remove spaces from column names
df.columns = df.columns.str.strip()

import numpy as np
# Replace infinity values with NaN
df.replace([np.inf, -np.inf], np.nan, inplace=True)

# Remove rows with NaN
df.dropna(inplace=True)

print("Dataset Shape:", df.shape)

print("Missing Values:")
print(df.isnull().sum().sum())

# Remove missing values
df = df.dropna()

# Separate features and target
X = df.drop("Label", axis=1)
y = df["Label"]

# Encode labels
encoder = LabelEncoder()
y = encoder.fit_transform(y)

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Model
model = XGBClassifier(
    n_estimators=100,
    max_depth=6,
    learning_rate=0.1
)

model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print(f"Accuracy: {accuracy*100:.2f}%")

# Save model
joblib.dump(model, "models/nids_model.pkl")

print("Model saved successfully!")