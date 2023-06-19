graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

visited = []  # List for visited nodes.
queue = []  # Initialize a queue

def bfs(visited, graph, node):  # function for BFS
    visited.append(node)
    queue.append(node)
    while queue:  # Creating loop to visit each node
        m = queue.pop(0)
        for n in graph[m]:
            if n not in visited:
                visited.append(n)
                queue.append(n)

print("Following is the Breadth-First Search")
bfs(visited, graph, '5')  # function calling
print(visited)

def dfs(graph, node, visited):  # function for dfs
    if node not in visited:
        visited.append(node)  # appending nodes to visited
        for n in graph[node]:
            dfs(graph, n, visited)  # recursive calling of dfs
    return visited

print("\nFollowing is the Depth-First Search")
visited = dfs(graph, '5', [])
print(visited)
