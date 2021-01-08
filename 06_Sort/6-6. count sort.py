# count sort : Fastest sort Algorithm
# 계수정렬 . 특정한경우에만 사용가능 ?
# O(N K)

array = [7, 5, 9, 3, 4, 5, 6, 7, 8, 9, 1, 3, 0, 45]
print(f"before :: {array}")

#  모든 범위를 포함하는 리스트 선언, 초기화
count = [0] * (max(array)+1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')