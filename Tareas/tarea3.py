import heapq

#Punto 1
def prim(graph, start):
    visit = set()
    pq = []
    visit.add(start)

    for vecino, w in graph[start]:
        heapq.heappush(pq, (w, start, vecino))
    
    mst = {}
    sum = 0

    while pq:
        w, padre, vertex = heapq.heappop(pq)
        if vertex not in visit:
            mst[padre] = vertex
            sum += w
            visit.add(vertex)
            for vecino, w in graph[vertex]:
                if vecino not in visit:
                    heapq.heappush(pq, (w, vertex, vecino))
    return mst, sum

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


def solPrim(graph, ini, fin):
    mst, sum = prim(graph, ini)
    tmp = ini
    print("Camino por MST:")
    while mst[tmp] != fin:
        print(tmp, end="->")
        tmp = mst[tmp]
    print(tmp, end="->")
    print(fin)

def solDijkstra(graph, ini, fin):
    d, pi = dijkstra(graph, ini)
    tmp = fin
    l = [tmp]
    print("Camino por dijkstra:")
    while pi[tmp] != ini:
        tmp = pi[tmp]
        l.append(tmp)
      
    l.append(ini)
    i = len(l) - 1
    while i >= 0:
        if(i != 0):
            print(l[i], end = "->")
        else:
            print(l[i])
        i -= 1
graph = {
    "pc1" : [("sw2", 1)],
    "sw2" : [("pc1", 1), ("sw1", 4), ("sw3", 4)],
    "sw1" : [("sw2", 4), ("sw3", 4), ("sw4", 4)],
    "sw3" : [("sw1", 4), ("sw2", 4)],
    "sw4" : [("sw1", 4), ("pc2", 1)],
    "pc2" : [("sw4", 1)]

}
G = {
    "a": [("b", 4), ("h", 8)],
    "b": [("a", 4), ("c", 8), ("h", 11)],
    "c": [("b", 8), ("d", 7), ("f", 4), ("i", 2)],
    "d": [("c", 7), ("e", 9), ("f", 14)],
    "e": [("d", 9), ("f", 10)],
    "f": [("c", 4), ("d", 14), ("e", 10), ("g", 2)],
    "g": [("f", 2), ("h", 1), ("i", 6)],
    "h": [("a", 8), ("b", 11), ("i", 7), ("g", 1)],
    "i": [("c", 2), ("g", 6), ("h", 7)]
}

""" mst, sum = prim(graph, "pc1")
print(mst)
 """
solDijkstra(graph, "pc1", "pc2")
solPrim(graph, "pc1", "pc2")