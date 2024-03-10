graph = {}
def add_node(v):
    if v in graph:
        print(v,"is in graph")
    else:
        graph[v] = []

def add_edge(v1,v2):
    if v1 not in graph:
        print(v1,"not in graph")
    elif v2 not in graph:
        print(v2, "not in graph")
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)

visited = []
queue = []
def BFS(node,visited,graph):
    visited.append(node)
    queue.append(node)
    while queue:
        m = queue.pop(0)
        print(m, end = " ")
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)




print(graph)
print("After")
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")
add_edge("A","B")
add_edge("B","E")
add_edge("A","C")
add_edge("A","D")
add_edge("B","D")
add_edge("C","D")
add_edge("E","D")
print(graph)
print("BFS")
BFS("A",visited,graph)



