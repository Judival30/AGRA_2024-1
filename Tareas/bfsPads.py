# Tarea 7 marzo
from collections import deque

#Punto 2
def bfs(graph, A, B):
    queue = deque()
    queue.append(A)
    countPads = 0
    while queue:
        vertex = queue.popleft()
        for neighbor in graph[vertex]:
            queue.append(neighbor)
            if neighbor == B:
                countPads += 1
                
    return countPads


graph = {
    'm': ['x', 'q', "r"],
    't': [],
    'q': ['t'],
    'n': ['q', "u", "o"],
    'x': [],
    'u': ["t"],
    "r" : ["u", "y"],
    "o" : ["r", "v", "s"],
    "p" : ["o", "s", "z"],
    "s" : ["r"],
    "v" : ["w", "x"],
    "y" : ["v"],
    "w" : ["z"],
    "z" : []
}
print(bfs(graph, "p", "v"))

#Punto 3
def bfs2(graph, A):
    queue = deque()
    queue.append(A)
    ans = True
    while queue and ans:
        vertex = queue.popleft()
        for neighbor in graph[vertex]:
            queue.append(neighbor)
            if neighbor == A:
                ans = False
                
    return not ans


graph2 = {
    'm': ['x', 'q', "r"],
    't': ["m"],
    'q': ['t'],
    'n': ['q', "u", "o"],
    'x': [],
    'u': ["t"],
    "r" : ["u", "y"],
    "o" : ["r", "v", "s"],
    "p" : ["o", "s", "z"],
    "s" : ["r"],
    "v" : ["w", "x"],
    "y" : ["v"],
    "w" : ["z"],
    "z" : []
}
print(bfs2(graph2, "m"))
print(bfs2(graph, "m"))
