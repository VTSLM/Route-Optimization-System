import osmnx as ox


def plot_real_route(G, route):

    fig, ax = ox.plot_graph_route(G, route)
