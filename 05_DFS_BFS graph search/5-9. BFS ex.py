# BFS Breadth First Search
# closed node will be visited early
from collections import deque

def bfs(graph, start, visited):
    # by Queue
    queue = deque([start])

    # now position will be visiting
    visited[start] = True

    # Loop until Queue will be empty
    while queue:
        # pop 1 node
        v = queue.popleft()
        print(v, end = ' ')

        # insert node with connected but not visited 2 queue
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True




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
bfs(graph, 1, visited)