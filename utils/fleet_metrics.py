def total_fleet_distance(fleet):

    total = 0

    for vehicle in fleet:
        total += vehicle.total_distance

    return total


def average_route_distance(fleet):

    if len(fleet) == 0:
        return 0

    return total_fleet_distance(fleet) / len(fleet)


def total_deliveries(fleet):

    total = 0

    for vehicle in fleet:
        total += len(vehicle.deliveries)

    return total
