class Vehicle:
    def __init__(self, vehicle_id):

        self.vehicle_id = vehicle_id

        self.deliveries = []

        self.route = []

        self.route_coordinates = []

        self.total_distance = 0

        self.total_eta = 0

        self.fuel_used = 0
