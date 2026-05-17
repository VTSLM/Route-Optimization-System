import math


def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def nearest_neighbor_tsp(points, start):
    unvisited = points.copy()
    route = [start]
    current = start
    unvisited.remove(start)
    while unvisited:
        nearest = min(unvisited, key=lambda point: distance(current, point))
        route.append(nearest)
        unvisited.remove(nearest)
        current = nearest
    route.append(start)  # return to the starting point
    return route


def route_cost(route):
    total_cost = 0
    for i in range(len(route) - 1):
        total_cost += distance(route[i], route[i + 1])
    return total_cost
