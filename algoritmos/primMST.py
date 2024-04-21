import heapq

#Punto 1
def prim(graph, start):
    visit = set()
    pq = []
    visit.add(start)

    for vecino, w in graph[start]:
        heapq.heappush(pq, (w, start, vecino))
    
    mst = []
    sum = 0

    while pq:
        w, padre, vertex = heapq.heappop(pq)
        if vertex not in visit:
            mst.append((padre, vertex))
            sum += w
            visit.add(vertex)
            for vecino, w in graph[vertex]:
                if vecino not in visit:
                    heapq.heappush(pq, (w, vertex, vecino))
    return mst, sum

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

mst, sum = prim(G, "a")
print("Árbol de abarcamiento mínimo:")
for edge in mst:
    print(edge)
print("Peso mínimo:", sum)


""" 
Punto 2
No puede existir un árbol abarcador mínimo con menos costo acumulado que A, ya que 
de ser el caso de que exista otro árbol con menos costo en realidad el primero no 
sería el mst, el árbol abarcador mínimo representa el costo mínimo para conectar 
todos los vértices del grafo, y no puede haber una opción más barata, de lo contrario, no sería mínimo.
"""
