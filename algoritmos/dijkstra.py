def dijkstra(graph, ini):
    d = {i : float('inf') for i in graph}
    pi = {v : None for v in graph}
    d[ini] = 0
    pq = [(0, ini)]

    while pq:
        curD, vertex = heapq.heappop(pq)
        for vecino, w in graph[vertex]:
            distance = curD + w
            if distance < d[vecino]:
                d[vecino] = distance
                pi[vecino] = vertex 
                heapq.heappush(pq, (distance, vecino))
    return d, pi
