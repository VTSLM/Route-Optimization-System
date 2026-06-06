import folium


def visualize_fleet(fleet):

    m = folium.Map(location=[23.0225, 72.5714], zoom_start=12)

    colors = ["blue", "red", "green", "purple", "orange"]

    for vehicle in fleet:
        color = colors[vehicle.vehicle_id % len(colors)]

        if len(vehicle.route_coordinates) < 2:
            continue

        folium.PolyLine(
            vehicle.route_coordinates,
            color=color,
            weight=5,
            tooltip=f"Vehicle {vehicle.vehicle_id}",
        ).add_to(m)

        folium.Marker(
            vehicle.route_coordinates[0],
            popup=f"Vehicle {vehicle.vehicle_id} Start",
            icon=folium.Icon(color=color),
        ).add_to(m)

    return m
