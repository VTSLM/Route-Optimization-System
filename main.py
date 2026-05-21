from ml.dataset_generator import generate_traffic_data
from ml.traffic_model import TrafficModel

df = generate_traffic_data()

print(df.head())


traffic_model = TrafficModel()

traffic_model.train(df)


eta = traffic_model.predict_eta(distance=10, hour=18, traffic_level=8, weather=1)


print(f"ETA: {eta:.2f} minutes")
