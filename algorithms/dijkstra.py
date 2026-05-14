import heapq


def dijkstra(graph, start):
    distances = {
        node: float("inf") for node in graph
    }  # initialize distances to all nodes as infinity
    distances[start] = 0
    pq = [(0, start)]  # priority queue to store (distance, node) pairs
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        # get the node with the smallest distance
        if current_distance > distances[current_node]:
            continue  # if the distance is greater than the recorded distance, skip
        for neighbor, weight in graph[current_node]:
            distance = (
                current_distance + weight
            )  # calculate the distance to the neighbor
            if distance < distances[neighbor]:
                distances[neighbor] = distance  # update the distance to the neighbor
                heapq.heappush(pq, (distance, neighbor))
    return distances
