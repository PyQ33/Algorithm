# 미로 탈출하기 위해 움직여야하는 최소 칸의 수
# BFS 로 함, # 시작점에서 가까운 노드부터 차례로 그래프의 모든 노드 탐색

from collections import deque

n, m = map(int, input().split())

# 2 dimention list map info
graph = []
for i in range(n):
    graph.append(list(map(int, input())))


# move direction Definition
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS
def bfs(x, y):
    # by Queue
    queue = deque()
    queue.append((x, y))

    # Loop until Queue will be empty
    while queue:
        x, y = queue.popleft()
        # from now node, 4 direction check

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # if out of maze, Ignore
            if nx <0 or ny <0 or nx >= n or ny >= m:
                continue

            # if barrier , Ignore
            if graph[nx][ny] == 0:
                continue

            # if now node visited at first
            if graph[nx][ny] ==1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    # until endtoRightm endtoDown, Shortest Distance
    return graph[n-1][m-1]

print(bfs(0,0))
# ------input
"""
5 6
101010
111111
000001
111111
111111
"""