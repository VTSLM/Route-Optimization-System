from algorithms.traffic_route_cost import traffic_route_distance, road_distance_meters


def nearest_neighbor_tsp(points, start, G):

    unvisited = points.copy()

    route = [start]

    current = start

    unvisited.remove(start)

    while unvisited:
        nearest = min(
            unvisited, key=lambda point: traffic_route_distance(G, current, point)
        )

        route.append(nearest)

        unvisited.remove(nearest)

        current = nearest

    route.append(start)

    return route


def route_cost(route, G):

    total_cost = 0

    for i in range(len(route) - 1):
        total_cost += road_distance_meters(G, route[i], route[i + 1])

    return total_cost
