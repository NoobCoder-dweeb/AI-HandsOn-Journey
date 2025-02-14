from queue import Queue

adj_list = {
    "A": ["B", "D"],
    "B": ["A", "C"],
    "C": ["B"],
    "D": ["A", "E", "F"],
    "E": ["D", "F", "G"],
    "F": ["D", "E", "H"],
    "G": ["E", "H"],
    "H": ["F", "G"]
}

def bfs():
    visited = {}
    level = {} # distance dictionary
    parent = {}
    bfs_traversal_output = []
    queue = Queue()

    # initialise visited and level
    for node in adj_list.keys():
        visited[node] = False
        parent[node] = None
        level[node] = -1 #inf

    print("Visited: ", visited)
    print("Level: ", level)
    print("Parent: ", parent)


    print('\n\nImplement BFS to print output')
    source = 'A'
    visited[source] = True
    level[source] = 0

    queue.put(source)

    while not queue.empty():
        # pop first element of queue
        u = queue.get()
        # add u as visited vertex
        bfs_traversal_output.append(u)

        # explore adjecent nodes of u
        for v in adj_list[u]:
            # check if the vertex is visited
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                level[v] = level[u] + 1

                queue.put(v)

    print("BFS Traversal: ", bfs_traversal_output)
    print("Level: ", level)

    # print("Level: ", level["G"]) # find distance of "G" from source "A"

    nodes = adj_list.keys()
    for node in nodes:
        if node != source:
            print(f"Shortest distance between A and {node} is {level[node]}")

    # shortest path from any node from source
    v = "G"
    path = [] # only works if graph is fully connected
    while v is not None:
        path.append(v)
        v = parent[v]
    path.reverse()

    print("Shortest path from A to G is: ", path)

if __name__ == "__main__":
    bfs()