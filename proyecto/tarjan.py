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



visited = [False for _ in range(50000)]
low = [-1 for _ in range(50000)]
p = [-1 for _ in range(50000)]
apNodes = set()
t, n = int(), int()


def ap():
    global low, visited, p
    for i in range(n):
        low[i] = visited[i] = p[i] = -1
   
    for i in range(n):
        if visited[i] == -1:
            apAux(i)
            

def apAux(v):
    global low, visited, p, apNodes, t
    num = 0
    t += 1
    visited[v] = low[v] = t

    for w in G[v]:
        if visited[w] == -1:
            num += 1
            p[w] = v
            apAux(w)
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
    global G, apNodes, n
    n = len(G)
    """ n, m = map(int, stdin.readline().split())

    for i in range(m):
        u, v = map(int, stdin.readline().split())
        G[u].append(v)
        G[v].append(u) """

    ap()

    if len(apNodes) == 0:
        print("No hay puntos de articulacion")
    else:
        print("Puntos de Articulacion:")
        print(*apNodes)
        inDegree = inDegreAP(apNodes, G)
        print("Seguidores")
        inDegree = dict(sorted(inDegree.items(), key=lambda item: item[1], reverse=True))
        for i in inDegree:
            print("Influencer %d, tiene %d seguidores" % (i, inDegree[i]))
        

main()