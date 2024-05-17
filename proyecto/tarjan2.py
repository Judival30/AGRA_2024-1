"""
Algoritmo de Tarjan (AP)

"""
from sys import stdin

#G = [[] for _ in range(50000)]
""" G = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6, 7],
    4: [2, 8, 9],
    5: [2, 10, 11],
    6: [3, 12, 13],
    7: [3, 14, 15],
    8: [4],
    9: [4],
    10: [5],
    11: [5],
    12: [6],
    13: [6],
    14: [7],
    15: [7]
} """


""" visited = [False for _ in range(50000)]
low = [-1 for _ in range(50000)]
p = [-1 for _ in range(50000)]
apNodes = set()
t, n = int(), int() """


def ap(graph):
    visited = {i : False for i in graph}
    low = {i : -1 for i in graph}
    p = {i : -1 for i in graph}
    apNodes = set()
    for i in graph:
        low[i] = visited[i] = p[i] = -1
    t = 0
    for i in graph:
        if visited[i] == -1:
            apAux(i, graph, visited, low, p, apNodes, t)
    return apNodes
            

def apAux(v, G, visited, low, p, apNodes, t):
    num = 0
    t += 1
    visited[v] = low[v] = t

    for w in G[v]:
        if visited[w] == -1:
            num += 1
            p[w] = v
            apAux(w, G, visited, low, p, apNodes, t)
            low[v] = min(low[v], low[w])

            #verificar si es un punto de articulacion
            if p[v] != -1 and low[w] >= visited[v]:
                apNodes.add(v)
                
        elif w != p[v]:
            low[v] = min(low[v], visited[w])

    if p[v] == -1 and num > 1:
        apNodes.add(v)
    

def inDegreAP(artiPoints, graph):
    ans = {i : len(graph[i]) for i in artiPoints}
    return ans



def main():
    """ n, m = map(int, stdin.readline().split())

    for i in range(m):
        u, v = map(int, stdin.readline().split())
        G[u].append(v)
        G[v].append(u) 
    G = {
    'A': ['B', 'G'],
    'B': ['C', 'D', 'A', 'F'],
    'C': ['B', 'D', 'E'],
    'D': ['B', 'C', 'E'],
    'E': ['C', 'D'],
    'F': ['B', 'G', 'H', 'I'],
    'G': ['A', 'F'],
    'H': ['F', 'I'],
    'I': ['F', 'H', 'J'],
    'J': ['I'],
    'K': ['L'],
    'L': ['K']
    }
    """
    G = {}
    key = stdin.readline().strip()
    while key != "":
        lst = key.split()
        G[lst[0]] = lst[1:]
        key = stdin.readline().strip()

    apNodes = ap(G)

    if len(apNodes) == 0:
        print("No hay puntos de articulacion")
    else:
        print("Puntos de Articulacion:")
        print(*apNodes)
        inDegree = inDegreAP(apNodes, G)
        print("Seguidores")
        inDegree = dict(sorted(inDegree.items(), key=lambda item: item[1], reverse=True))
        for i in inDegree:
            print("Influencer %s, tiene %d seguidores" % (str(i), inDegree[i]))
    

main()