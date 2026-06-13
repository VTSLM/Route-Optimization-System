import osmnx as ox

from fastapi import APIRouter

from algorithms.route_optimizer import RouteOptimizer

from ml.real_eta_model import predict_eta
from utils.helpers import route_length
from utils.traffic_metrics import average_route_traffic

from simulation.traffic_simulation import apply_traffic_to_graph

from datetime import datetime


router = APIRouter()


# load graph once
G = ox.graph_from_place("Ahmedabad, India", network_type="drive")

G = apply_traffic_to_graph(G, datetime.now().hour)

optimizer = RouteOptimizer(G)


@router.get("/route")
def get_route(
    origin_lat: float, origin_lon: float, destination_lat: float, destination_lon: float
):

    origin_node = optimizer.coordinates_to_node(origin_lat, origin_lon)

    destination_node = optimizer.coordinates_to_node(destination_lat, destination_lon)

    distance_route = optimizer.shortest_route(origin_node, destination_node)

    distance_route_coordinates = []

    for node in distance_route:
        lat = G.nodes[node]["y"]

        lon = G.nodes[node]["x"]

        distance_route_coordinates.append([lat, lon])

    traffic_route = ox.shortest_path(
        G, origin_node, destination_node, weight="traffic_weight"
    )
    traffic_route_coordinates = []

    for node in traffic_route:
        lat = G.nodes[node]["y"]

        lon = G.nodes[node]["x"]

        traffic_route_coordinates.append([lat, lon])
    distance_length = route_length(G, distance_route)

    traffic_length = route_length(G, traffic_route)
    
    shortest_traffic = average_route_traffic(G, distance_route)

    traffic_route_traffic = average_route_traffic(G, traffic_route)
    hour = datetime.now().hour

    day_of_week = datetime.now().weekday()

    shortest_eta_seconds = predict_eta(
        distance_length / 1000, hour, day_of_week, shortest_traffic
    )

    traffic_eta_seconds = predict_eta(
        traffic_length / 1000, hour, day_of_week, traffic_route_traffic
    )

    eta_distance = shortest_eta_seconds / 60

    eta_traffic = traffic_eta_seconds / 60
    return {
        # shortest-distance route
        "shortest_route": {
            "distance_meters": distance_length,
            "eta_minutes": eta_distance,
            "traffic_level": shortest_traffic,
            "route_coordinates": distance_route_coordinates,
            "nodes": len(distance_route),
        },
        # traffic-aware route
        "traffic_aware_route": {
            "distance_meters": traffic_length,
            "eta_minutes": eta_traffic,
            "traffic_level": traffic_route_traffic,
            "route_coordinates": traffic_route_coordinates,
            "nodes": len(traffic_route),
        },
    }
