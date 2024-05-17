def tarjan_articulation_points(graph):
    """
    Esta función utiliza el algoritmo de Tarjan para encontrar los puntos de articulación en un grafo no dirigido.

    :param graph: Un diccionario que representa un grafo no dirigido, donde cada clave es un vértice y el valor asociado es una lista de vértices adyacentes.
    :return: Una lista de vértices que son puntos de articulación.
    """
    index = 0
    indices = {}
    lowlinks = {}
    articulation_points = set()
    visited = set()
    
    def dfs(v, parent=None):
        nonlocal index
        visited.add(v)
        indices[v] = index
        lowlinks[v] = index
        index += 1
        children = 0
        
        for neighbor in graph[v]:
            if neighbor == parent:
                continue
            if neighbor not in visited:
                children += 1
                dfs(neighbor, v)
                lowlinks[v] = min(lowlinks[v], lowlinks[neighbor])
                
                # Articulation point found via bridge
                if parent is not None and lowlinks[neighbor] >= indices[v]:
                    articulation_points.add(v)
            else:
                lowlinks[v] = min(lowlinks[v], indices[neighbor])
        
        # Special case for root
        if parent is None and children > 1:
            articulation_points.add(v)
    
    for vertex in graph:
        if vertex not in visited:
            dfs(vertex)
    
    return list(articulation_points)

# Ejemplo de uso del algoritmo
G = {
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
}

print(tarjan_articulation_points(G))