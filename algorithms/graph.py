class Graph:
    def __init__(self):
        self.graph = {}  # empty dictionary(representing adjacency list) created

    def add_edge(self, u, v, weight):
        if u not in self.graph:  # check if node is in the graph
            self.graph[u] = []  # if not, then declare an empty list for that node
        if v not in self.graph:
            self.graph[v] = []  # if not, then declare an empty list for that node
        self.graph[u].append((v, weight))  # add v,weight to the list of u
        self.graph[v].append(
            (u, weight)
        )  # add u,weight to the list of v (undirected graph)

    def display(self):
        for node in self.graph:
            print(node, "->", self.graph[node])  # display node along with its list
