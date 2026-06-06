import random


def generate_deliveries(center_lat, center_lon, n=20):

    deliveries = []

    for _ in range(n):
        lat = center_lat + random.uniform(-0.03, 0.03)

        lon = center_lon + random.uniform(-0.03, 0.03)

        deliveries.append((lat, lon))

    return deliveries
