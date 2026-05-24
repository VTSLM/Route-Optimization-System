import osmnx as ox
import matplotlib.pyplot as plt


def plot_route(G, route, title):

    fig, ax = ox.plot_graph_route(G, route, show=False, close=False)

    plt.title(title)

    plt.show()
