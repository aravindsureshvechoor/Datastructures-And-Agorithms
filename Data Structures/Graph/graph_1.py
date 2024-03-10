nodes = []
graph = []
node_count = 0
def add_node(v):
    global node_count
    if v in nodes:
        print(v,"is already in graph")
    else:
        node_count += 1
        nodes.append(v)
        for n in graph:
            n.append(0)
        temp = []
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)

def add_edge(v1,v2):
    if v1 not in nodes:
        print(v1,"not in graph")
    elif v2 not in nodes:
        print(v2,"not in graph")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = 1
        graph[index2][index1] = 1


def delete(v):
    if v not in nodes:
        print("Node is not in graph")
    else:
        index = nodes.index(v)
        nodes.pop(index)
        for n in graph:
            n.pop(index)
        graph.pop(index)

def delete_edge(v1,v2):
    if v1 not in nodes:
        print(v1,"is not in graph")
    elif v2 not in nodes:
        print(v2, "is not in graph")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = 0
        graph[index2][index1] = 0



print(nodes)
print(graph)
print("After")
add_node("A")
add_node("B")
# add_node("C")
add_edge("A","B")
# add_edge("A","C")
print(nodes)
print(graph)
# print("After deletion")
# delete("B")
# print(nodes)
# print(graph)
# delete_edge("A","C")
# print("""delete_edge("A","C")""")
# print(graph)
