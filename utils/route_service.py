import osmnx as ox
from datetime import datetime

from algorithms.route_optimizer import RouteOptimizer
from ml.real_eta_model import predict_eta
from utils.helpers import route_length
from utils.traffic_metrics import average_route_traffic
from simulation.traffic_simulation import apply_traffic_to_graph


# Load graph only once
G = ox.graph_from_place("Ahmedabad, India", network_type="drive")
G = apply_traffic_to_graph(G, datetime.now().hour)

optimizer = RouteOptimizer(G)


def compute_routes(
    origin_lat,
    origin_lon,
    destination_lat,
    destination_lon,
):
    # Convert coordinates to graph nodes
    origin_node = optimizer.coordinates_to_node(origin_lat, origin_lon)
    destination_node = optimizer.coordinates_to_node(
        destination_lat,
        destination_lon,
    )

    # Shortest-distance route
    distance_route = optimizer.shortest_route(
        origin_node,
        destination_node,
    )

    distance_route_coordinates = []

    for node in distance_route:
        distance_route_coordinates.append([
            G.nodes[node]["y"],
            G.nodes[node]["x"],
        ])

    # Traffic-aware route
    traffic_route = ox.shortest_path(
        G,
        origin_node,
        destination_node,
        weight="traffic_weight",
    )

    traffic_route_coordinates = []

    for node in traffic_route:
        traffic_route_coordinates.append([
            G.nodes[node]["y"],
            G.nodes[node]["x"],
        ])

    # Route lengths
    distance_length = route_length(G, distance_route)
    traffic_length = route_length(G, traffic_route)

    # Average traffic factor
    shortest_traffic = average_route_traffic(G, distance_route)
    traffic_route_traffic = average_route_traffic(G, traffic_route)

    # Current time
    hour = datetime.now().hour
    day_of_week = datetime.now().weekday()

    # ETA prediction
    shortest_eta_seconds = predict_eta(
        distance_length / 1000,
        hour,
        day_of_week,
        shortest_traffic,
    )

    traffic_eta_seconds = predict_eta(
        traffic_length / 1000,
        hour,
        day_of_week,
        traffic_route_traffic,
    )

    return {
        "shortest_route": {
            "distance_meters": distance_length,
            "eta_minutes": shortest_eta_seconds / 60,
            "traffic_level": shortest_traffic,
            "route_coordinates": distance_route_coordinates,
            "nodes": len(distance_route),
        },
        "traffic_aware_route": {
            "distance_meters": traffic_length,
            "eta_minutes": traffic_eta_seconds / 60,
            "traffic_level": traffic_route_traffic,
            "route_coordinates": traffic_route_coordinates,
            "nodes": len(traffic_route),
        },
    }
