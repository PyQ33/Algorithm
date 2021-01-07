# position of horse at now

input_data = input()
row = int(input_data[1])
col = int(ord(input_data[0])) - int(ord('a')) + 1
print(row, col)

## 아스키코드 to 문자   : chr()
##  문자 to 아스키코드  : ord()

# Can Step move of 8 directions
##  부분집합 구하기 _______
steps = [
    (-2,1),
    (-1,-2),
    (1,-2),
    (2,-1),
    (2,1),
    (1,2),
    (-1,2),
    (-2,1)
]

# check  can move
result = 0
for step in steps:
    next_row = row + step[0]
    next_col = col + step[1]

    # 좌표로 이동가능한 조건이면, 횟수 카운트 +
    if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
        result += 1

print(result)