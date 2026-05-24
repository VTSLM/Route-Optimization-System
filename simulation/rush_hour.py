def rush_hour_multiplier(hour):

    # morning rush
    if 7 <= hour <= 10:
        return 2.5

    # evening rush
    elif 17 <= hour <= 20:
        return 3.0

    # normal traffic
    return 1.0
