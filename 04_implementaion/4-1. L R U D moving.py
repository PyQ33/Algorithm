
# n input

#n = int(input())
n = int(100)
x, y  = 1, 1
#plans = input().split()
plans = "R R R U D D".split()
print(plans)

# 좌우상하  Left Right Up Down  따른 이동방향 Direction_Cell
dx = [0, 0, -1, 1] # 좌우 ?
dy = [-1, 1, 0, 0] # 상하 ?
# Let 오른쪽 방향이 +1 R 인경우 
# Let 아래로 방향이 +1 D 인경우
# + Row == + Down
# + Col == + Right
##  좌표 : (Row +-U/D, Col +- R/L)

move_types = list(map(str, "L R U D".split()))
print(move_types)

# moving plans check
for plan in plans:
    # After move, 좌표
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i] # dx는 변화량, nx 는 next 좌표, x 는 현재좌표
            ny = y + dy[i]

    # if out of range PASS
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    # Move
    x, y = nx, ny
print(x, y)
