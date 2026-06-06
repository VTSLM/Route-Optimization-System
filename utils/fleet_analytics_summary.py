def total_fleet_eta(fleet):

    return sum(vehicle.total_eta for vehicle in fleet)


def total_fuel_used(fleet):

    return sum(vehicle.fuel_used for vehicle in fleet)
