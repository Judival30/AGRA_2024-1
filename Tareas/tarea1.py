from collections import deque

multiGraph = {
    1 : [2, 2, 4],
    2 : [1, 4, 4],
    3 : [4, 4],
    4 : [1, 2, 2, 3]
}

graph1 = {
    "A" : ["C", "E", "B"],
    "B" : ["E", "D"], 
    "C" : [],
    "D" : ["C"],
    "E" : ["C"]
}

graph2 = {
    1 : [2],
    2 : [3,4],
    3 : [5,6],
    4 : [7,8],
    5 : [],
    6 : [9, 10],
    7 : [10],
    8 : [10],
    9 : [],
    10 : []
}

emptyGraph = {}

#Punto 3
def clearMultiG(graph):
    """ Recibe un Multigrafo y retorna un grafo
    el cual no tiene aristas repetidas ni aristas que 
    apuntan así mismo

    Args:
        graph (dict): diccionario de listas

    Returns:
        dict(set): diccionarios de conjuntos
    """
    ans = {i: set() for i in graph}
    for vertex in graph:
        for vecino in graph[vertex]:
            if vertex != vecino:
                ans[vertex].add(vecino)
                ans[vecino].add(vertex)
    return ans

print("Funcion clearMultiG")
print("multiGraph",clearMultiG(multiGraph))
print("graph1", clearMultiG(graph1))
print("graph2", clearMultiG(graph2))
print("emptyGraph", clearMultiG(emptyGraph))


#Punto 4
def bfsCountLevel(graph, start, level, ans : dict):
    """ Recorre el grafo por amplitud

    Args:
        graph (dict): diccionarios de listas
        start (int / string): Nodo de inicio
        level (int): longitud deseada
        ans (dict): diccionario de conjuntos
    """
    queue = deque([(start, 0)])
    while queue:
        node, node_level = queue.popleft()

        if node_level == level:
            ans[start].add(node)

        for neighbor in graph[node]:
            queue.append((neighbor, node_level + 1))


def graphGradeN(graph, n):
    """ Recibe un grafo y un valor n que 
    representa el grado del grafo que se quiere
    retornar

    Args:
        graph (dict(list)): diccionario de listas
        n (int): nivel deseado

    Returns:
        dicc(set): diccionarios de listas
    """
    ans = {i : set() for i in graph}
    for vertex in graph:
        bfsCountLevel(graph, vertex, n, ans) 
    return ans

print("Funcion graphGradeN")
print("graph1", graphGradeN(graph1, 2))
print("graph2", graphGradeN(graph2, 3))
print("emptyGraph",graphGradeN(emptyGraph, 4))