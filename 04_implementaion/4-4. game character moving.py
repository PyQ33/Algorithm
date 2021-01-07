# 맵생성
# 현재 row, col 좌표에서  direction 방향을 보고서있음
# 지도 모양 입력,  1 : 바다 or 벽 , 0 : 이동가능

# index : 북 동 남 서
# index : [0, 1, 2, 3]

# n, m
n, m = map(int, input().split())

# 방문한 위치 저장 위한 맵생성, 초기화
d = [[0] * m for _ in range(n)]

# now character x, y, direction
x, y, direction = map(int, input().split())

d[x][y] = 1
# now position visited

# total map info
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북 남 동 서 방향정의
# left 2  right 1 up 4  down 3
## dx, dy 방향 정의하는법 ?

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# turn left
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction =3

# simulator start
count =1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    # after turn, if no visited cell is
    if d[nx][ny] ==0 and array[nx][ny] ==0:
        d[nx][ny] =1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue

    # after turn, no visited cell not, or cant go
    else:
        turn_time +=1

    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if array[nx][ny] == 0:
            x = nx
            y = ny

        else:
            break
        turn_time = 0

print(count)