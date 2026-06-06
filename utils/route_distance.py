from math import sqrt


def route_distance(route):

    total = 0

    for i in range(len(route) - 1):
        lat1, lon1 = route[i]

        lat2, lon2 = route[i + 1]

        total += sqrt((lat2 - lat1) ** 2 + (lon2 - lon1) ** 2)

    return total
