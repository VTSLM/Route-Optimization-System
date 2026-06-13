import osmnx as ox


def average_route_traffic(G, route):

    total_ratio = 0
    edge_count = 0

    for stop1, stop2 in zip(route[:-1], route[1:]):
        lat1, lon1 = stop1
        lat2, lon2 = stop2

        node1 = ox.distance.nearest_nodes(G, lon1, lat1)

        node2 = ox.distance.nearest_nodes(G, lon2, lat2)

        road_route = ox.shortest_path(G, node1, node2, weight="traffic_weight")

        if road_route is None:
            continue

        for u, v in zip(road_route[:-1], road_route[1:]):
            edge_data = G.get_edge_data(u, v)

            if edge_data is None:
                continue

            edge = edge_data[0]

            length = edge.get("length", 1)

            traffic_weight = edge.get("traffic_weight", length)

            ratio = traffic_weight / length

            total_ratio += ratio

            edge_count += 1

    if edge_count == 0:
        return 1

    return total_ratio / edge_count
