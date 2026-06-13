import sys
import os

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if project_root not in sys.path:
    sys.path.insert(0, project_root)

import streamlit as st

from streamlit_folium import st_folium

from simulation.delivery_generator import generate_deliveries

from algorithms.vehicle_clustering import cluster_deliveries

from simulation.fleet_manager import create_fleet

from algorithms.tsp import nearest_neighbor_tsp, route_cost

from visualization.fleet_visualization import visualize_fleet

from utils.fleet_metrics import (
    total_fleet_distance,
    average_route_distance,
    total_deliveries,
)

from utils.build_route_geometry import build_route_geometry

from utils.fleet_analytics import estimate_eta, estimate_fuel

from utils.fleet_analytics_summary import total_fleet_eta, total_fuel_used

import osmnx as ox

from datetime import datetime

from simulation.traffic_simulation import apply_traffic_to_graph

from utils.traffic_metrics import average_route_traffic

from ml.real_eta_model import predict_eta


@st.cache_resource
def load_graph():

    G = ox.graph_from_place("Ahmedabad, India", network_type="drive")

    G = apply_traffic_to_graph(G, datetime.now().hour)

    return G


G = load_graph()

st.set_page_config(page_title="Fleet Dashboard", layout="wide")

st.title("🚚 Fleet Management Dashboard")

# ----------------------------
# USER INPUTS
# ----------------------------

num_deliveries = st.slider("Number of Deliveries", 10, 50, 20)

num_vehicles = st.slider("Number of Vehicles", 1, 10, 3)


# ----------------------------
# GENERATE DATA
# ----------------------------

deliveries = generate_deliveries(23.0225, 72.5714, num_deliveries)

clusters = cluster_deliveries(deliveries, num_vehicles)

fleet = create_fleet(clusters)


# ----------------------------
# ROUTE OPTIMIZATION
# ----------------------------

for vehicle in fleet:
    if len(vehicle.deliveries) < 2:
        continue

    start = vehicle.deliveries[0]

    optimized_route = nearest_neighbor_tsp(vehicle.deliveries, start, G)

    vehicle.route = optimized_route

    vehicle.route_coordinates = build_route_geometry(G, optimized_route)

    st.write(f"Vehicle {vehicle.vehicle_id}")

    st.write(f"Stops: {len(vehicle.route)}")

    vehicle.total_distance = route_cost(optimized_route, G)

    # route_cost is in coordinate units
    # treat as approximate km for demo

    traffic_level = average_route_traffic(G, optimized_route)

    vehicle.traffic_level = traffic_level

    distance_km = vehicle.total_distance / 1000

    hour = datetime.now().hour

    day_of_week = datetime.now().weekday()

    eta_seconds = predict_eta(distance_km, hour, day_of_week, traffic_level)

    vehicle.total_eta = eta_seconds / 60

    vehicle.fuel_used = estimate_fuel(distance_km)

# ----------------------------
# GLOBAL METRICS
# ----------------------------

st.header("Fleet Overview")

col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

with col1:
    st.metric("Vehicles", len(fleet))

with col2:
    st.metric("Deliveries", total_deliveries(fleet))

with col3:
    st.metric("Fleet Distance", f"{total_fleet_distance(fleet):.3f}")

with col4:
    st.metric("Avg Route", f"{average_route_distance(fleet):.3f}")
with col5:
    st.metric("Fleet ETA", f"{total_fleet_eta(fleet):.1f} min")

with col6:
    st.metric("Fuel Used", f"{total_fuel_used(fleet):.2f} L")
with col7:
    st.metric("Avg Traffic", f"{sum(v.traffic_level for v in fleet) / len(fleet):.1f}")
# ----------------------------
# VEHICLE DETAILS
# ----------------------------

st.header("Vehicle Statistics")

for vehicle in fleet:
    with st.expander(f"Vehicle {vehicle.vehicle_id}"):
        st.write(f"Deliveries: {len(vehicle.deliveries)}")

        st.write(f"Distance: {vehicle.total_distance:.4f}")

        st.write(f"ETA: {vehicle.total_eta:.1f} min")

        st.write(f"Fuel Used: {vehicle.fuel_used:.2f} L")

        st.write(f"Stops: {len(vehicle.route) - 1}")

        st.write(f"Traffic Level: {vehicle.traffic_level}")

        st.write("Route:")

        st.write(vehicle.route)


# ----------------------------
# MAP
# ----------------------------

st.header("Fleet Map")

fleet_map = visualize_fleet(fleet)

st_folium(fleet_map, width=1200, height=600, returned_objects=[])
