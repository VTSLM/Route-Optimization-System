import osmnx as ox


def build_route_geometry(G, stops):

    coordinates = []

    for i in range(len(stops) - 1):
        lat1, lon1 = stops[i]

        lat2, lon2 = stops[i + 1]

        node1 = ox.distance.nearest_nodes(G, lon1, lat1)

        node2 = ox.distance.nearest_nodes(G, lon2, lat2)

        route = ox.shortest_path(G, node1, node2, weight="traffic_weight")

        if route is None:
            print(f"No path found between {stops[i]} and {stops[i + 1]}")
            continue

        for node in route:
            coordinates.append([G.nodes[node]["y"], G.nodes[node]["x"]])

    return coordinates
