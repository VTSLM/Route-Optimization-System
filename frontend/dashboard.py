import streamlit as st
import requests
import folium

from streamlit_folium import st_folium


# m = folium.Map(location=[23.0225, 72.5714], zoom_start=12)
# st_folium(m, width=700, height=500)

st.title("Intelligent Route Optimization System")


origin_lat = st.number_input("Origin Latitude", value=23.0225)

origin_lon = st.number_input("Origin Longitude", value=72.5714)

destination_lat = st.number_input("Destination Latitude", value=23.0400)

destination_lon = st.number_input("Destination Longitude", value=72.5900)


if st.button("Compute Route"):
    try:
        response = requests.get(
            "http://127.0.0.1:8000/route",
            params={
                "origin_lat": origin_lat,
                "origin_lon": origin_lon,
                "destination_lat": destination_lat,
                "destination_lon": destination_lon,
            },
        )

        data = response.json()
        if "error" in data:
            st.error(data["error"])

            st.stop()
        shortest_route = data["shortest_route"]

        traffic_route = data["traffic_aware_route"]

        # shortest route coordinates
        shortest_coordinates = []

        for coord in shortest_route["route_coordinates"]:
            lat = float(coord[0])

            lon = float(coord[1])

            shortest_coordinates.append([lat, lon])

        # traffic-aware coordinates
        traffic_coordinates = []

        for coord in traffic_route["route_coordinates"]:
            lat = float(coord[0])

            lon = float(coord[1])

            traffic_coordinates.append([lat, lon])

        st.header("Route Comparison")

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Shortest Route")

            st.metric("Distance", f"{shortest_route['distance_meters'] / 1000:.2f} km")

            st.metric("ETA", f"{shortest_route['eta_minutes']:.2f} min")

            st.metric("Nodes", shortest_route["nodes"])
        with col2:
            st.subheader("Traffic-Aware Route")

            st.metric("Distance", f"{traffic_route['distance_meters'] / 1000:.2f} km")

            st.metric("ETA", f"{traffic_route['eta_minutes']:.2f} min")

            st.metric("Nodes", traffic_route["nodes"])

        st.header("Recommendation")
        if traffic_route["eta_minutes"] < shortest_route["eta_minutes"]:
            st.success("Traffic-Aware Route is Faster")

        else:
            st.success("Shortest Route is Faster")
            # create map
        m = folium.Map(location=shortest_coordinates[0], zoom_start=13)

        # SHORTEST ROUTE
        # blue

        folium.PolyLine(
            locations=shortest_coordinates,
            weight=5,
            color="blue",
            tooltip=("Shortest Distance Route"),
        ).add_to(m)

        # TRAFFIC-AWARE ROUTE
        # red

        folium.PolyLine(
            locations=traffic_coordinates,
            weight=5,
            color="red",
            tooltip=("Traffic-Aware Route"),
        ).add_to(m)

        # origin marker
        folium.Marker(
            shortest_coordinates[0], popup="Origin", icon=folium.Icon(color="green")
        ).add_to(m)

        # destination marker
        folium.Marker(
            shortest_coordinates[-1],
            popup="Destination",
            icon=folium.Icon(color="darkred"),
        ).add_to(m)

        # render map
        st_folium(m, width=700, height=500, returned_objects=[])

    except Exception as e:
        st.error(str(e))
