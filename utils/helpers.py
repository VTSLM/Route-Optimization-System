def route_length(G, route):

    total = 0

    for u, v in zip(route[:-1], route[1:]):
        edge_data = G.get_edge_data(u, v)[0]

        total += edge_data["length"]

    return total
