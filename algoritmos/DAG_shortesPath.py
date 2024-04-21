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
