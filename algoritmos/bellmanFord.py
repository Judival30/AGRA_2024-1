def bellmanFord(graph, ini):
    d = {i : float('inf') for i in graph}
    pi = {v : None for v in graph}
    d[ini] = 0

    for _ in range(len(graph) - 1):
        for u in graph:
            for v, w in graph[u].items():
                if d[u] + w < d[v]:
                    d[v] = d[u] + w
                    pi[v] = u
    for u in graph:
        for v, w in graph[u].items():
            if d[u] + w < d[v]:
                return False
    return d, pi
