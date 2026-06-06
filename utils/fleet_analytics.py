def estimate_eta(distance_km, average_speed=30):
    """
    distance_km : route distance in km
    average_speed : km/hr

    returns ETA in minutes
    """

    hours = distance_km / average_speed

    return hours * 60


def estimate_fuel(distance_km, mileage=15):
    """
    mileage = km per litre
    """

    return distance_km / mileage
