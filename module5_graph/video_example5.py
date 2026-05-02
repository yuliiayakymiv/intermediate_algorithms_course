def countComponents(n, edges):
    def dfs(node):
        # If the node is already visited, return to avoid cycles
        if visited[node]:
            return
        visited[node] = True
        for neighbor in graph[node]:
            dfs(neighbor)

    # Initialize a graph represented as an adjacency list
    graph = {i: [] for i in range(n)}

    # Populate the graph with the given edges
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * n
    components = 0

    # Iterate through each node in the graph
    for i in range(n):
        # If a node is unvisited, it's part of a new component
        if not visited[i]:
            dfs(i)
            components += 1

    return components
