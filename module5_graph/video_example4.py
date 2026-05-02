def validTree(n, edges):
    # Check for the necessary condition of a tree (n-1 edges)
    if len(edges) != n - 1:
        return False

    # Create an adjacency list
    graph = {i: [] for i in range(n)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()

    def dfs(node, parent):
        if node in visited:
            return False
        visited.add(node)

        for neighbor in graph[node]:
            # Ignore the edge leading back to the parent
            if neighbor == parent:
                continue

            # Attempt to visit all neighbors. Return False if a cycle is found.
            if not dfs(neighbor, node):
                return False

        return True

    # Start DFS from node 0; Check if it's fully connected and has no cycle
    return dfs(0, -1) and len(visited) == n
