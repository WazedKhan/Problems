n = 3
source = 0
destination = 2
edges = [[0,1],[1,2],[2,0]]

def validPath(n, source, destination, edges):
    graph = build_graph(edges)
    return hasPath(graph, source, destination, set())

def hasPath(graph, src, dst, visited):
    if src == dst:return True
    if src in visited: return False
    visited.add(src)
    for neighbor in graph[src]:
        if hasPath(graph, neighbor, dst, visited) == True:
            return True
    return False



def build_graph(edges):
    graph = {}

    for edge in edges:
        a, b = edge
        if a not in graph: graph[a] = []
        if b not in graph: graph[b] = []
        graph[a].append(b)
        graph[b].append(a)

    return graph

print(validPath(n, source, destination, edges))