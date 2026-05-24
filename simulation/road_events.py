import random


def apply_road_closures(G, closure_probability=0.01):

    for u, v, k, data in G.edges(keys=True, data=True):
        # randomly close roads
        if random.random() < closure_probability:
            data["closed"] = True

            # massive weight penalty
            data["traffic_weight"] = 1e9

        else:
            data["closed"] = False

    return G


def apply_accidents(G, accident_probability=0.02):

    for u, v, k, data in G.edges(keys=True, data=True):
        if random.random() < accident_probability:
            data["accident"] = True

            accident_penalty = random.uniform(5, 20)

            data["traffic_weight"] *= accident_penalty

        else:
            data["accident"] = False

    return G
