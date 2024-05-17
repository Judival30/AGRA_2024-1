import random

def generate_large_directed_graph(nodes, percentage):
    """
    Genera un grafo dirigido con listas de adyacencia usando un diccionario.
    Cada nodo tiene una lista de nodos a los cuales está conectado mediante un arco dirigido.

    :param num_nodes: Número de nodos en el grafo.
    :param arc_percentage: Porcentaje del número total de arcos posibles que deben ser incluidos en el grafo.
    :return: Un diccionario representando el grafo dirigido.
    """
    lines = []
    lst = []
    with open("c:\\Users\\judiv\\OneDrive\\Escritorio\\Universidad\\Semestre_4\\Agra\\proyecto\\names.txt", 'r') as file:
        lines = file.readlines()
    random_number = random.randint(1, 999)
    for i in range(0,nodes):
        lst.append(lines[random_number - 1].strip())
        random_number = random.randint(1, 999)

    graph = {lst[i]: [] for i in range(nodes)}

    possibleArcs = nodes * (nodes - 1)
    numArcs = int(possibleArcs * percentage / 100)
    currentArcs = 0

    while currentArcs < numArcs:
        u = random.randint(0, nodes - 1)
        v = random.randint(0, nodes - 1)
        if u != v and lst[v] not in graph[lst[u]]:
            graph[lst[u]].append(lst[v])
            currentArcs += 1

    return graph

graph = generate_large_directed_graph(500,0.5)

with open("c:\\Users\\judiv\\OneDrive\\Escritorio\\Universidad\\Semestre_4\\Agra\\proyecto\\graph.txt", 'w') as file:
    for key in graph:
        s = str(key) + " "
        for name in graph[key]:
            s += name
            s += " "
        s += "\n"
        file.write(s)
