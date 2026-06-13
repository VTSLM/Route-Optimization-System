from simulation.delivery_generator import generate_deliveries

from algorithms.vehicle_clustering import cluster_deliveries

from simulation.fleet_manager import create_fleet

from visualization.fleet_visualization import visualize_fleet

from utils.fleet_metrics import (
    total_fleet_distance,
    average_route_distance,
    total_deliveries,
)
from utils.build_route_geometry import build_route_geometry
import time
from ml.real_eta_model import predict_eta
from utils.traffic_metrics import average_route_traffic
from algorithms.tsp import nearest_neighbor_tsp, route_cost
import osmnx as ox

from datetime import datetime

from simulation.traffic_simulation import apply_traffic_to_graph

hour = datetime.now().hour

G = ox.graph_from_place("Ahmedabad, India", network_type="drive")

G = apply_traffic_to_graph(G, hour)
# -----------------------------------
# STEP 1
# Generate deliveries
# -----------------------------------

deliveries = generate_deliveries(center_lat=23.0225, center_lon=72.5714, n=20)

print(f"Generated {len(deliveries)} deliveries")


# -----------------------------------
# STEP 2
# Cluster deliveries
# -----------------------------------

num_vehicles = 3

clusters = cluster_deliveries(deliveries, num_vehicles)

print(f"Created {num_vehicles} clusters")


# -----------------------------------
# STEP 3
# Create fleet
# -----------------------------------

fleet = create_fleet(clusters)

print(f"Created {len(fleet)} vehicles")


# -----------------------------------
# STEP 4
# Assign routes
# -----------------------------------

for vehicle in fleet:
    deliveries = vehicle.deliveries

    if len(deliveries) < 2:
        continue

    start = deliveries[0]

    start_time = time.time()

    optimized_route = nearest_neighbor_tsp(deliveries, start, G)

    end_time = time.time()

    print("TSP Time:", end_time - start_time, "seconds")

    vehicle.route = optimized_route

    vehicle.route_coordinates = build_route_geometry(G, optimized_route)

    vehicle.total_distance = route_cost(optimized_route, G)

    traffic_level = average_route_traffic(G, optimized_route)

    distance_km = vehicle.total_distance / 1000

    hour = datetime.now().hour

    day_of_week = datetime.now().weekday()

    eta_seconds = predict_eta(distance_km, hour, day_of_week, traffic_level)

    vehicle.total_eta = eta_seconds / 60

# -----------------------------------
# STEP 5
# Print vehicle details
# -----------------------------------

for vehicle in fleet:
    print()

    print(f"Vehicle {vehicle.vehicle_id}")

    print(f"Deliveries: {len(vehicle.deliveries)}")

    print(f"Distance: {vehicle.total_distance:.4f}")

    print(f"ETA: {vehicle.total_eta:.2f} minutes")

    print(f"Stops: {len(vehicle.route) - 1}")

    for stop in vehicle.route:
        print(stop)
# -----------------------------------
# STEP 6
# Fleet analytics
# -----------------------------------

print()

print("Total Fleet Distance:", total_fleet_distance(fleet))

print("Average Route Distance:", average_route_distance(fleet))

print("Total Deliveries:", total_deliveries(fleet))

print("Route:")


# -----------------------------------
# STEP 7
# Visualize fleet
# -----------------------------------

m = visualize_fleet(fleet)

m.save("fleet_map.html")

print()

print("Fleet map saved as fleet_map.html")
