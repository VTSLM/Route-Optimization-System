from simulation.delivery_generator import generate_deliveries

from algorithms.vehicle_clustering import cluster_deliveries

from simulation.fleet_manager import create_fleet

from visualization.fleet_visualization import visualize_fleet

from utils.route_distance import route_distance

from utils.fleet_metrics import (
    total_fleet_distance,
    average_route_distance,
    total_deliveries,
)


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
    # TEMPORARY
    # Until TSP is integrated

    vehicle.route = vehicle.deliveries

    vehicle.route_coordinates = []

    for lat, lon in vehicle.route:
        vehicle.route_coordinates.append([lat, lon])

    vehicle.total_distance = route_distance(vehicle.route)


# -----------------------------------
# STEP 5
# Print vehicle details
# -----------------------------------

for vehicle in fleet:
    print()

    print(f"Vehicle {vehicle.vehicle_id}")

    print(f"Deliveries: {len(vehicle.deliveries)}")

    print(f"Distance: {vehicle.total_distance:.4f}")


# -----------------------------------
# STEP 6
# Fleet analytics
# -----------------------------------

print()

print("Total Fleet Distance:", total_fleet_distance(fleet))

print("Average Route Distance:", average_route_distance(fleet))

print("Total Deliveries:", total_deliveries(fleet))


# -----------------------------------
# STEP 7
# Visualize fleet
# -----------------------------------

m = visualize_fleet(fleet)

m.save("fleet_map.html")

print()

print("Fleet map saved as fleet_map.html")
