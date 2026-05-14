import osmnx as ox
import matplotlib.pyplot as plt


place_name = "Ahmedabad, India"

G = ox.graph_from_place(place_name, network_type="drive")

print(G)

# fig, ax = ox.plot_graph(G)

origin = list(G.nodes)[890]
destination = list(G.nodes)[50000]

route = ox.shortest_path(G, origin, destination)

fig, ax = ox.plot_graph_route(G, route)
