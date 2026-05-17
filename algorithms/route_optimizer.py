import osmnx as ox


class RouteOptimizer:
    def __init__(self, graph):

        self.graph = graph

    def coordinates_to_node(self, lat, lon):

        return ox.distance.nearest_nodes(self.graph, lon, lat)

    def shortest_route(self, node1, node2):

        return ox.shortest_path(self.graph, node1, node2, weight="length")
