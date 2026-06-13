import pandas as pd
import numpy as np
import joblib

from math import radians
from math import sin
from math import cos
from math import sqrt
from math import atan2

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error


def haversine(lat1, lon1, lat2, lon2):

    R = 6371

    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)

    a = (
        sin(dlat / 2) ** 2
        + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    )

    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c


print("Loading dataset...")

df = pd.read_csv("data/train.csv", nrows=100000)  # Load a subset for faster training

print("Dataset loaded")

# -------------------
# Datetime features
# -------------------

df["pickup_datetime"] = pd.to_datetime(df["pickup_datetime"])

df["hour"] = df["pickup_datetime"].dt.hour

df["day_of_week"] = df["pickup_datetime"].dt.dayofweek

# -------------------
# Simulated Traffic
# -------------------

np.random.seed(42)

df["traffic_level"] = np.random.randint(1, 11, size=len(df))

# -------------------
# Distance feature
# -------------------

print("Calculating distances...")

df["distance_km"] = df.apply(
    lambda row: haversine(
        row["pickup_latitude"],
        row["pickup_longitude"],
        row["dropoff_latitude"],
        row["dropoff_longitude"],
    ),
    axis=1,
)

# -------------------
# Features
# -------------------

features = ["distance_km", "hour", "day_of_week", "traffic_level"]

X = df[features]

df["adjusted_duration"] = df["trip_duration"] * (1 + 0.05 * (df["traffic_level"] - 1))
y = df["adjusted_duration"]

# -------------------
# Split
# -------------------

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -------------------
# Train
# -------------------

print("Training model...")

model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)

model.fit(X_train, y_train)

# -------------------
# Evaluate
# -------------------

predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)

print(f"MAE: {mae:.2f} seconds")

# -------------------
# Save model
# -------------------

joblib.dump(model, "ml/eta_model.pkl")

print("Model saved!")
