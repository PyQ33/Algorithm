# n , m input
n, m = map(int, input().split())

# 2 dimention list map info

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# by DFS, a node will be visited & connected node will be visited
def dfs(x, y):
    # if outrange break
    if x <= -1 or x >= n or y<=-1 or y >= m:
        return False

    # if not visited now node
    if graph[x][y] == 0:
        # visit
        graph[x][y] = 1
        # L D R U will be visited
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

# all node will be visited (water)
result = 0

for i in range(n):
    for j in range(m):
        # start DFS
        if dfs(i,j) == True:
            result += 1

print(result)
