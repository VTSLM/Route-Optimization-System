import osmnx as ox


class ReroutingEngine:
    def __init__(self, graph):

        self.graph = graph

    def reroute(self, origin, destination):

        return ox.shortest_path(
            self.graph, origin, destination, weight="traffic_weight"
        )
