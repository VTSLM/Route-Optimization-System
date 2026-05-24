import random

from simulation.rush_hour import rush_hour_multiplier


def apply_traffic_to_graph(G, hour):

    rush_multiplier = rush_hour_multiplier(hour)

    for u, v, k, data in G.edges(keys=True, data=True):
        base_traffic = random.uniform(1, 3)

        traffic_factor = base_traffic * rush_multiplier

        data["traffic_weight"] = data["length"] * traffic_factor

    return G
