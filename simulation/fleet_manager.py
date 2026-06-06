from simulation.vehicle import Vehicle


def create_fleet(clusters):

    fleet = []

    for cluster_id in clusters:
        vehicle = Vehicle(cluster_id)

        vehicle.deliveries = clusters[cluster_id]

        fleet.append(vehicle)

    return fleet
