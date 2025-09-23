from collections import deque
graph = {}
def add_node(node):
    if node not in graph:
        graph[node] = []

def add_edge(u, v):
    if u in graph and v in graph:
        graph[u].append(v)

def bfs(start_node):
    visited = set()
    queue = deque([start_node])
    print("Visited nodes in BFS order:")

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)


for i in range(6):
    add_node(i)
    add_edge(0, 1)
    add_edge(0, 2)
    add_edge(1, 3)
    add_edge(2, 4)
    add_edge(3, 5)
    bfs(0)
