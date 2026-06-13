import osmnx as ox


def traffic_route_distance(G, point1, point2):

    lat1, lon1 = point1

    lat2, lon2 = point2

    node1 = ox.distance.nearest_nodes(G, lon1, lat1)

    node2 = ox.distance.nearest_nodes(G, lon2, lat2)

    route = ox.shortest_path(G, node1, node2, weight="traffic_weight")

    if route is None:
        return float("inf")

    distance = 0

    for u, v in zip(route[:-1], route[1:]):
        edge = G.get_edge_data(u, v)[0]

        distance += edge.get("traffic_weight", edge["length"])

    return distance
