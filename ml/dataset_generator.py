import pandas as pd
import random


def generate_traffic_data(samples=1000):

    data = []

    for _ in range(samples):
        distance = random.uniform(1, 20)

        hour = random.randint(0, 23)

        traffic_level = random.randint(1, 10)

        weather = random.randint(0, 1)

        speed = 40 - traffic_level * 2 - weather * 5

        speed = max(speed, 5)

        eta = (distance / speed) * 60

        data.append([distance, hour, traffic_level, weather, eta])

    columns = ["distance", "hour", "traffic_level", "weather", "eta"]

    return pd.DataFrame(data, columns=columns)
