# DFS

def dfs(graph, v, visited):

    # now position will be visiting
    visited[v] = True
    print(v, end=' ')

    # now node & other node visiting
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# each nodes connection info 2 list (2 dimension matrix)

graph = [
    [], # start
    [2, 3, 8],  # at 1
    [1, 7],  # at 2
    [1,4, 5] , # at 3
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7] # at 8
]

# each node info 2 list of visited
visited = [False] * 9

# dfs funtion import
dfs(graph, 1, visited)
