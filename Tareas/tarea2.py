import heapq
import time

""" Coclusiones: 
En el grafo 1 de las diapositivas no es posible determinar un camino de minimo
costo ya que contiene ciclos negativos, el único algoritmo que nos brindaría 
un resultado sería el bellmanFord pero retornaría un False

En el caso del segundo grafo de las diapositivas nos encontramos que sirven los 3 
algoritmos al ser un grafo aciclico, por lo cual no tendríamos el problema de ciclos 
negativos. Al correr los 3 algoritmos se oberva que el más eficiente es el DAG, sin 
embargo está muy cerca de dijkstra, mientras que si se nota una gran diferencia con 
respecto al bellmanFord. 

Las diferencias entre los tiempos de estos algoritmos se debe a su complejidad temporal
el bellmanFord al poseer la peor cota de complejidad es el que más se demora al realizar
la verificación de los ciclos negativos además de recorrer todos los nodos v - 1 veces.
En segundo lugar, tenemos a dijkstra, y su complejidad radica en la cola de prioridad
ya que al tratarse de un monticulo esta complejidad se vuelve logaritmica, pero se asume 
que no van a haber ciclos negativos. En ultimo lugar, y con mejor tiempo de ejecucición 
está el DAD, al radicar su complejidad en el topoSort, sin embargo es un caso muy condicionado
al no permitir ni siquiera ciclos negativos.

"""
def dijkstra(graph, ini):
    d = {i : float('inf') for i in graph}
    pi = {v : None for v in graph}
    d[ini] = 0
    pq = [(0, ini)]

    while pq:
        curD, vertex = heapq.heappop(pq)
        for vecino, w in graph[vertex].items():
            distance = curD + w
            if distance < d[vecino]:
                d[vecino] = distance
                pi[vecino] = vertex 
                heapq.heappush(pq, (distance, vecino))
    return d, pi

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

def dfs(graph, node, visited, ans):

    visited[node] = True
    for vecino in graph[node]:
        if not visited[vecino]:
            dfs(graph, vecino, visited, ans)
    ans.append(node)

def topologicalSort(graph):
    
    visited = {i : False for i in graph}
    topoLst = []

    for node in graph:
        if not visited[node]:
            dfs(graph, node, visited, topoLst )

    return topoLst[::-1]

def DAG_shortesPath(graph, ini):
    d = {i : float('inf') for i in graph}
    pi = {v : None for v in graph}
    d[ini] = 0
    topoLst = topologicalSort(graph)
    for vertex in topoLst:
        for vecino, w in graph[vertex].items():
            if d[vertex] + w < d[vecino]:
                    d[vecino] = d[vertex] + w
                    pi[vecino] = vertex
    return d, pi


graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 3, 'B': 2, 'D': 4, 'E': 2},
    'D': {'B': 1, 'C': 4, 'E': 1, 'F': 5},
    'E': {'C': 2, 'D': 1, 'F': 4},
    'F': {'D': 5, 'E': 4}
}   

graphDAG = {
    'A': {'B': 9, 'C': 3},
    'B': {'C': 2, 'D': 1},
    'C': {'D': 4, 'E': 2},
    'D': {'E': 1, 'F': 5},
    'E': {'F': 4},
    'F': {}
}
grafo = {
    1: {2: 4, 3: 9, 4: 7, 5: 3, 6: 2, 7: 8, 8: 6, 9: 5, 10: 1, 11: 10, 12: 12, 13: 15, 14: 11, 15: 14},
    2: {1: 4, 3: 5, 4: 11, 5: 9, 6: 10, 7: 14, 8: 8, 9: 7, 10: 3, 11: 6, 12: 13, 13: 16, 14: 12, 15: 15},
    3: {1: 9, 2: 5, 4: 2, 5: 8, 6: 7, 7: 11, 8: 5, 9: 4, 10: 10, 11: 3, 12: 14, 13: 17, 14: 13, 15: 16},
    4: {1: 7, 2: 11, 3: 2, 5: 6, 6: 5, 7: 9, 8: 3, 9: 2, 10: 8, 11: 1, 12: 13, 13: 16, 14: 12, 15: 15},
    5: {1: 3, 2: 9, 3: 8, 4: 6, 6: 4, 7: 8, 8: 2, 9: 1, 10: 7, 11: 2, 12: 12, 13: 15, 14: 11, 15: 14},
    6: {1: 2, 2: 10, 3: 7, 4: 5, 5: 4, 7: 6, 8: 4, 9: 3, 10: 9, 11: 4, 12: 14, 13: 17, 14: 13, 15: 16},
    7: {1: 8, 2: 14, 3: 11, 4: 9, 5: 8, 6: 6, 8: 2, 9: 1, 10: 7, 11: 2, 12: 12, 13: 15, 14: 11, 15: 14},
    8: {1: 6, 2: 8, 3: 5, 4: 3, 5: 2, 6: 4, 7: 2, 9: 4, 10: 8, 11: 1, 12: 13, 13: 16, 14: 12, 15: 15},
    9: {1: 5, 2: 7, 3: 4, 4: 2, 5: 1, 6: 3, 7: 1, 8: 4, 10: 6, 11: 3, 12: 14, 13: 17, 14: 13, 15: 16},
    10: {1: 1, 2: 3, 3: 10, 4: 8, 5: 7, 6: 9, 7: 7, 8: 8, 9: 6, 11: 5, 12: 13, 13: 16, 14: 12, 15: 15},
    11: {1: 10, 2: 6, 3: 3, 4: 1, 5: 2, 6: 4, 7: 2, 8: 1, 9: 3, 10: 5, 12: 12, 13: 15, 14: 11, 15: 14},
    12: {1: 12, 2: 13, 3: 14, 4: 13, 5: 12, 6: 14, 7: 12, 8: 13, 9: 14, 10: 13, 11: 12, 13: 16, 14: 12, 15: 15},
    13: {1: 15, 2: 16, 3: 17, 4: 16, 5: 15, 6: 17, 7: 15, 8: 16, 9: 17, 10: 16, 11: 15, 12: 16, 14: 8, 15: 11},
    14: {1: 11, 2: 12, 3: 13, 4: 12, 5: 11, 6: 13, 7: 11, 8: 12, 9: 13, 10: 12, 11: 11, 12: 12, 13: 8, 15: 5},
    15: {1: 14, 2: 15, 3: 16, 4: 15, 5: 14, 6: 16, 7: 14, 8: 15, 9: 16, 10: 15, 11: 14, 12: 15, 13: 11, 14: 5}
}
grafo2 = {
    1: {2: 4, 3: 9, 4: 7, 5: 3, 6: 2, 7: 8, 8: 6, 9: 5, 10: 1, 11: 10, 12: 12, 13: 15, 14: 11, 15: 14, 16: 8, 17: 3, 18: 5, 19: 6, 20: 4, 21: 7, 22: 2, 23: 9, 24: 10, 25: 11, 26: 13, 27: 16, 28: 14, 29: 15, 30: 10},
    2: {1: 4, 3: 5, 4: 11, 5: 9, 6: 10, 7: 14, 8: 8, 9: 7, 10: 3, 11: 6, 12: 13, 13: 16, 14: 12, 15: 15, 16: 6, 17: 8, 18: 7, 19: 9, 20: 11, 21: 5, 22: 12, 23: 4, 24: 3, 25: 10, 26: 13, 27: 2, 28: 14, 29: 1, 30: 16},
    3: {1: 9, 2: 5, 4: 2, 5: 8, 6: 7, 7: 11, 8: 5, 9: 4, 10: 10, 11: 3, 12: 14, 13: 17, 14: 13, 15: 16, 16: 2, 17: 1, 18: 3, 19: 12, 20: 9, 21: 15, 22: 6, 23: 7, 24: 8, 25: 4, 26: 5, 27: 11, 28: 10, 29: 13, 30: 16},
    4: {1: 7, 2: 11, 3: 2, 5: 6, 6: 5, 7: 9, 8: 3, 9: 2, 10: 8, 11: 1, 12: 13, 13: 16, 14: 12, 15: 15, 16: 3, 17: 6, 18: 4, 19: 8, 20: 1, 21: 2, 22: 5, 23: 9, 24: 10, 25: 7, 26: 11, 27: 12, 28: 14, 29: 13, 30: 15},
    5: {1: 3, 2: 9, 3: 8, 4: 6, 6: 4, 7: 8, 8: 2, 9: 1, 10: 7, 11: 2, 12: 12, 13: 15, 14: 11, 15: 14, 16: 9, 17: 10, 18: 11, 19: 6, 20: 7, 21: 3, 22: 4, 23: 8, 24: 5, 25: 12, 26: 1, 27: 13, 28: 14, 29: 15, 30: 16},
    6: {1: 2, 2: 10, 3: 7, 4: 5, 5: 4, 7: 6, 8: 4, 9: 3, 10: 9, 11: 4, 12: 14, 13: 17, 14: 13, 15: 16, 16: 5, 17: 6, 18: 7, 19: 8, 20: 9, 21: 10, 22: 11, 23: 12, 24: 13, 25: 14, 26: 15, 27: 16, 28: 17, 29: 18, 30: 19},
    7: {1: 8, 2: 14, 3: 11, 4: 9, 5: 8, 6: 6, 8: 2, 9: 1, 10: 7, 11: 2, 12: 12, 13: 15, 14: 11, 15: 14, 16: 10, 17: 3, 18: 6, 19: 8, 20: 9, 21: 13, 22: 4, 23: 5, 24: 15, 25: 16, 26: 18, 27: 19, 28: 11, 29: 20, 30: 21},
    8: {1: 6, 2: 8, 3: 5, 4: 3, 5: 2, 6: 4, 7: 2, 9: 4, 10: 8, 11: 1, 12: 13, 13: 16, 14: 12, 15: 15, 16: 7, 17: 9, 18: 10, 19: 11, 20: 12, 21: 14, 22: 16, 23: 17, 24: 18, 25: 19, 26: 20, 27: 21, 28: 22, 29: 23, 30: 24},
    9: {1: 5, 2: 7, 3: 4, 4: 2, 5: 1, 6: 3, 7: 1, 8: 4, 10: 6, 11: 3, 12: 14, 13: 17, 14: 13, 15: 16, 16: 8, 17: 9, 18: 10, 19: 11, 20: 12, 21: 13, 22: 14, 23: 15, 24: 16, 25: 17, 26: 18, 27: 19, 28: 20, 29: 21, 30: 22},
    10: {1: 1, 2: 3, 3: 10, 4: 8, 5: 7, 6: 9, 7: 7, 8: 8, 9: 6, 11: 5, 12: 13, 13: 16, 14: 12, 15: 15, 16: 7, 17: 8, 18: 9, 19: 10, 20: 11, 21: 12, 22: 13, 23: 14, 24: 15, 25: 16, 26: 17, 27: 18, 28: 19, 29: 20, 30: 21},
    11: {1: 10, 2: 6, 3: 3, 4: 1, 5: 2, 6: 4, 7: 2, 8: 1, 9: 3, 10: 5, 12: 12, 13: 15, 14: 11, 15: 14, 16: 12, 17: 14, 18: 10, 19: 11, 20: 9, 21: 8, 22: 7, 23: 6, 24: 5, 25: 4, 26: 3, 27: 2, 28: 1, 29: 16, 30: 17},
    12: {1: 12, 2: 13, 3: 14, 4: 13, 5: 12, 6: 14, 7: 12, 8: 13, 9: 14, 10: 13, 11: 12, 13: 16, 14: 12, 15: 15, 16: 11, 17: 10, 18: 9, 19: 8, 20: 7, 21: 6, 22: 5, 23: 4, 24: 3, 25: 2, 26: 1, 27: 17, 28: 18, 29: 19, 30: 20},
    13: {1: 15, 2: 16, 3: 17, 4: 16, 5: 15, 6: 17, 7: 15, 8: 16, 9: 17, 10: 16, 11: 15, 12: 16, 14: 8, 15: 11, 16: 13, 17: 14, 18: 15, 19: 16, 20: 17, 21: 18, 22: 19, 23: 20, 24: 21, 25: 22, 26: 23, 27: 24, 28: 25, 29: 26, 30: 27},
    14: {1: 11, 2: 12, 3: 13, 4: 12, 5: 11, 6: 13, 7: 11, 8: 12, 9: 13, 10: 12, 11: 11, 12: 12, 13: 8, 15: 5, 16: 14, 17: 15, 18: 16, 19: 17, 20: 18, 21: 19, 22: 20, 23: 21, 24: 22, 25: 23, 26: 24, 27: 25, 28: 26, 29: 27, 30: 28},
    15: {1: 14, 2: 15, 3: 16, 4: 15, 5: 14, 6: 16, 7: 14, 8: 15, 9: 16, 10: 15, 11: 14, 12: 15, 13: 11, 14: 5, 16: 15, 17: 16, 18: 17, 19: 18, 20: 19, 21: 20, 22: 21, 23: 22, 24: 23, 25: 24, 26: 25, 27: 26, 28: 27, 29: 28, 30: 29},
    16: {1: 8, 2: 6, 3: 2, 4: 3, 5: 9, 6: 5, 7: 10, 8: 7, 9: 8, 10: 7, 11: 12, 12: 11, 13: 13, 14: 14, 15: 15, 17: 16, 18: 17, 19: 18, 20: 19, 21: 20, 22: 21, 23: 22, 24: 23, 25: 24, 26: 25, 27: 26, 28: 27, 29: 28, 30: 29},
    17: {1: 3, 2: 8, 3: 1, 4: 6, 5: 10, 6: 6, 7: 3, 8: 9, 9: 9, 10: 8, 11: 14, 12: 10, 13: 14, 14: 15, 15: 16, 16: 16, 18: 17, 19: 18, 20: 19, 21: 20, 22: 21, 23: 22, 24: 23, 25: 24, 26: 25, 27: 26, 28: 27, 29: 28, 30: 29},
    18: {1: 5, 2: 7, 3: 3, 4: 4, 5: 11, 6: 7, 7: 6, 8: 10, 9: 10, 10: 9, 11: 15, 12: 11, 13: 15, 14: 16, 15: 17, 16: 17, 17: 17, 19: 18, 20: 19, 21: 20, 22: 21, 23: 22, 24: 23, 25: 24, 26: 25, 27: 26, 28: 27, 29: 28, 30: 29},
    19: {1: 6, 2: 9, 3: 12, 4: 8, 5: 6, 6: 8, 7: 8, 8: 11, 9: 11, 10: 10, 11: 16, 12: 12, 13: 16, 14: 17, 15: 18, 16: 18, 17: 18, 18: 18, 20: 19, 21: 20, 22: 21, 23: 22, 24: 23, 25: 24, 26: 25, 27: 26, 28: 27, 29: 28, 30: 29},
    20: {1: 4, 2: 11, 3: 9, 4: 1, 5: 7, 6: 9, 7: 9, 8: 12, 9: 12, 10: 11, 11: 17, 12: 13, 13: 17, 14: 18, 15: 19, 16: 19, 17: 19, 18: 19, 19: 19, 21: 20, 22: 21, 23: 22, 24: 23, 25: 24, 26: 25, 27: 26, 28: 27, 29: 28, 30: 29},
    21: {1: 7, 2: 5, 3: 15, 4: 2, 5: 3, 6: 10, 7: 13, 8: 14, 9: 13, 10: 12, 11: 13, 12: 14, 13: 18, 14: 19, 15: 20, 16: 20, 17: 20, 18: 20, 19: 20, 20: 20, 22: 21, 23: 22, 24: 23, 25: 24, 26: 25, 27: 26, 28: 27, 29: 28, 30: 29},
    22: {1: 2, 2: 12, 3: 6, 4: 5, 5: 4, 6: 11, 7: 4, 8: 16, 9: 14, 10: 13, 11: 7, 12: 15, 13: 19, 14: 20, 15: 21, 16: 21, 17: 21, 18: 21, 19: 21, 20: 21, 21: 21, 23: 22, 24: 23, 25: 24, 26: 25, 27: 26, 28: 27, 29: 28, 30: 29},
    23: {1: 9, 2: 4, 3: 7, 4: 9, 5: 8, 6: 12, 7: 5, 8: 17, 9: 15, 10: 14, 11: 6, 12: 16, 13: 20, 14: 21, 15: 22, 16: 22, 17: 22, 18: 22, 19: 22, 20: 22, 21: 22, 22: 22, 24: 23, 25: 24, 26: 25, 27: 26, 28: 27, 29: 28, 30: 29},
    24: {1: 10, 2: 3, 3: 8, 4: 10, 5: 5, 6: 13, 7: 15, 8: 18, 9: 16, 10: 15, 11: 5, 12: 17, 13: 21, 14: 22, 15: 23, 16: 23, 17: 23, 18: 23, 19: 23, 20: 23, 21: 23, 22: 23, 23: 23, 25: 24, 26: 25, 27: 26, 28: 27, 29: 28, 30: 29},
    25: {1: 11, 2: 10, 3: 4, 4: 7, 5: 12, 6: 14, 7: 16, 8: 19, 9: 17, 10: 16, 11: 4, 12: 18, 13: 22, 14: 23, 15: 24, 16: 24, 17: 24, 18: 24, 19: 24, 20: 24, 21: 24, 22: 24, 23: 24, 24: 24, 26: 25, 27: 26, 28: 27, 29: 28, 30: 29},
    26: {1: 13, 2: 13, 3: 5, 4: 11, 5: 1, 6: 15, 7: 18, 8: 20, 9: 18, 10: 17, 11: 3, 12: 19, 13: 23, 14: 24, 15: 25, 16: 25, 17: 25, 18: 25, 19: 25, 20: 25, 21: 25, 22: 25, 23: 25, 24: 25, 25: 25, 27: 26, 28: 27, 29: 28, 30: 29},
    27: {1: 16, 2: 2, 3: 11, 4: 12, 5: 13, 6: 16, 7: 19, 8: 21, 9: 19, 10: 18, 11: 2, 12: 20, 13: 24, 14: 25, 15: 26, 16: 26, 17: 26, 18: 26, 19: 26, 20: 26, 21: 26, 22: 26, 23: 26, 24: 26, 25: 26, 26: 26, 28: 27, 29: 28, 30: 29},
    28: {1: 14, 2: 14, 3: 10, 4: 13, 5: 14, 6: 17, 7: 11, 8: 22, 9: 20, 10: 19, 11: 1, 12: 21, 13: 25, 14: 26, 15: 27, 16: 27, 17: 27, 18: 27, 19: 27, 20: 27, 21: 27, 22: 27, 23: 27, 24: 27, 25: 27, 26: 27, 27: 27, 29: 28, 30: 29},
    29: {1: 15, 2: 1, 3: 13, 4: 14, 5: 15, 6: 18, 7: 20, 8: 23, 9: 21, 10: 20, 11: 16, 12: 22, 13: 26, 14: 27, 15: 28, 16: 28, 17: 28, 18: 28, 19: 28, 20: 28, 21: 28, 22: 28, 23: 28, 24: 28, 25: 28, 26: 28, 27: 28, 28: 28, 30: 29},
    30: {1: 10, 2: 16, 3: 16, 4: 15, 5: 16, 6: 19, 7: 21, 8: 24, 9: 22, 10: 21, 11: 17, 12: 23, 13: 27, 14: 28, 15: 29, 16: 29, 17: 29, 18: 29, 19: 29, 20: 29, 21: 29, 22: 29, 23: 29, 24: 29, 25: 29, 26: 29, 27: 29, 28: 29, 29: 29}
}
grafoDiapo1 = {
    "s" : {"a" : 3, "e" : 2, "c" : 5},
    "e" : {"f" : 3},
    "c" : {"d" : 6},
    "a" : {"b" : -4},
    "b" : {"g" : 4},
    "d" : {"c" : - 3, "g" : 8},
    "f" : {"e" : -6, "g" : 7}, 
    "g" : {}
}

grafoDiapo2 = {
    'm': {'x' : 2, 'q': 4, "r" : 10},
    't': {},
    'q': {'t' : 12},
    'n': {'q' : 6, "u" : 14, "o" :3},
    'x': {},
    'u': {"t" : 9},
    "r" : {"u" : 3, "y" : 14},
    "o" : {"r" : 7, "v" :5, "s" : 21},
    "p" : {"o" : 6, "s" : 1, "z": 11},
    "s" : {"r" : 4},
    "v" : {"w" : 3, "x" : 8},
    "y" : {"v" : 4},
    "w" : {"z" : 8},
    "z" : {}
}
algoritmos = {"dijkstra" : dijkstra, "bellmanFord" : bellmanFord, "DAG_shortesPath" : DAG_shortesPath}
for i in algoritmos:
    tiempoInicial = time.perf_counter()
    d, pi = algoritmos[i](grafo2, 1)
    tiempoFinal = time.perf_counter()

    print("Tiempo en ", i, ":")
    print("%0.30f" % (tiempoFinal - tiempoInicial))

print("//////////////////////////////\nGrafo diapositiva 2")
print("recorrido desde m")
for i in algoritmos:
    tiempoInicial = time.perf_counter()
    d, pi = algoritmos[i](grafoDiapo2, "m")
    tiempoFinal = time.perf_counter()

    print("Tiempo en ", i, ":")
    print("%0.30f" % (tiempoFinal - tiempoInicial))

print("////////////////////////////////////\nrecorrido desde o")
for i in algoritmos:
    tiempoInicial = time.perf_counter()
    d, pi = algoritmos[i](grafoDiapo2, "o")
    tiempoFinal = time.perf_counter() 
    print("Tiempo en ", i, ":")
    print("%0.30f" % (tiempoFinal - tiempoInicial))
    for p, h in pi.items():
        print("padre", p, "hijo", h)
    for v, d in d.items():
        print("distancia minima desde", v, ":", d)

print("////////////////////////\nGrafo diapositiva 1")
print("Recorrido desde s")
lst = bellmanFord(grafoDiapo1, "s")
if type(lst) == bool:
    print("Tiene ciclos negativos")
else:
    distances, pi = lst
    print(distances, pi)

print("Recorrido desde e")
lst = bellmanFord(grafoDiapo1, "s")
if type(lst) == bool:
    print("Tiene ciclos negativos")
else:
    distances, pi = lst
    print(distances, pi)