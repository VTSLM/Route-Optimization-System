import heapq


def heuristic(a, b):
    return abs(ord(a) - ord(b))


def a_star(graph, start, goal):
    pq = [(0, start)]
    g_cost = {node: float("inf") for node in graph}
    g_cost[start] = 0
    while pq:
        f_cost, current_node = heapq.heappop(pq)
        if current_node == goal:
            return g_cost[goal]
        for neighbor, weight in graph[current_node]:
            tentative_g_cost = g_cost[current_node] + weight
            if tentative_g_cost < g_cost[neighbor]:
                g_cost[neighbor] = tentative_g_cost
                f_cost = tentative_g_cost + heuristic(neighbor, goal)
                heapq.heappush(pq, (f_cost, neighbor))
    return None
