import osmnx as ox

from fastapi import APIRouter

from algorithms.route_optimizer import RouteOptimizer

from ml.traffic_model import TrafficModel
from utils.helpers import route_length

from ml.dataset_generator import generate_traffic_data

traffic_model = TrafficModel()
df = generate_traffic_data()
traffic_model.train(df)
router = APIRouter()


# load graph once
G = ox.graph_from_place("Ahmedabad, India", network_type="drive")

optimizer = RouteOptimizer(G)


@router.get("/route")
@router.get("/route")
def get_route(
    origin_lat: float, origin_lon: float, destination_lat: float, destination_lon: float
):

    origin_node = optimizer.coordinates_to_node(origin_lat, origin_lon)

    destination_node = optimizer.coordinates_to_node(destination_lat, destination_lon)

    route = optimizer.shortest_route(origin_node, destination_node)

    distance_route_coordinates = []

    for node in route:
        lat = G.nodes[node]["y"]

        lon = G.nodes[node]["x"]

        distance_route_coordinates.append([lat, lon])

    distance_route = ox.shortest_path(G, origin_node, destination_node, weight="length")

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
    eta_distance = traffic_model.predict_eta(
        distance=distance_length / 1000, hour=18, traffic_level=7, weather=0
    )
    eta_traffic = traffic_model.predict_eta(
        distance=traffic_length / 1000, hour=18, traffic_level=3, weather=0
    )

    return {
        # shortest-distance route
        "shortest_route": {
            "distance_meters": distance_length,
            "eta_minutes": eta_distance,
            "traffic_level": "Heavy",
            "route_coordinates": distance_route_coordinates,
            "nodes": len(distance_route),
        },
        # traffic-aware route
        "traffic_aware_route": {
            "distance_meters": traffic_length,
            "eta_minutes": eta_traffic,
            "traffic_level": "Moderate",
            "route_coordinates": traffic_route_coordinates,
            "nodes": len(traffic_route),
        },
    }
