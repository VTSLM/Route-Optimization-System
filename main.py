import osmnx as ox

from simulation.traffic_simulation import apply_traffic_to_graph

from visualization.map_visualization import plot_route

from utils.helpers import route_length


# STEP 1
# Load Ahmedabad road graph

G = ox.graph_from_place("Ahmedabad, India", network_type="drive")


# STEP 2
# Apply simulated traffic

G = apply_traffic_to_graph(G)


# STEP 3
# Choose coordinates

origin_lat = 23.0225
origin_lon = 72.5714

destination_lat = 23.0400
destination_lon = 72.5900


# STEP 4
# Convert coordinates to nearest graph nodes

origin = ox.distance.nearest_nodes(G, origin_lon, origin_lat)

destination = ox.distance.nearest_nodes(G, destination_lon, destination_lat)


# STEP 5
# Compute shortest-distance route

distance_route = ox.shortest_path(G, origin, destination, weight="length")


# STEP 6
# Compute traffic-aware route

traffic_route = ox.shortest_path(G, origin, destination, weight="traffic_weight")


# STEP 7
# Compute route distances

distance_route_length = route_length(G, distance_route)

traffic_route_length = route_length(G, traffic_route)


# STEP 8
# Print results

print("Shortest Distance Route Length:")
print(f"{distance_route_length:.2f} meters")

print()

print("Traffic-Aware Route Length:")
print(f"{traffic_route_length:.2f} meters")


# STEP 9
# Visualize routes

print("\nDisplaying shortest-distance route...")

plot_route(G, distance_route, "Shortest Distance Route")

print("\nDisplaying traffic-aware route...")

plot_route(G, traffic_route, "Traffic-Aware Route")
