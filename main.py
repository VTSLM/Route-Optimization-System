import osmnx as ox

from algorithms.route_optimizer import RouteOptimizer

from simulation.delivery_simulation import simulate_delivery

from visualization.map_visualization import plot_real_route

from utils.helpers import route_length


# STEP 1
# Load Ahmedabad road graph

G = ox.graph_from_place("Ahmedabad, India", network_type="drive")


# STEP 2
# Create delivery coordinates

delivery_points = [
    (23.0225, 72.5714),
    (23.0300, 72.5800),
    (23.0150, 72.5600),
    (23.0400, 72.5900),
]


# STEP 3
# Initialize optimizer

optimizer = RouteOptimizer(G)


# STEP 4
# Convert coordinates to graph nodes

delivery_nodes = []

for lat, lon in delivery_points:
    node = optimizer.coordinates_to_node(lat, lon)

    delivery_nodes.append(node)


print("Delivery Nodes:")
print(delivery_nodes)


# STEP 5
# Compute shortest route between first two points

route = optimizer.shortest_route(delivery_nodes[0], delivery_nodes[1])


# STEP 6
# Compute route distance

distance = route_length(G, route)

print(f"Route Distance: {distance:.2f} meters")


# STEP 7
# Simulate delivery

simulate_delivery(delivery_nodes)


# STEP 8
# Visualize route

plot_real_route(G, route)
