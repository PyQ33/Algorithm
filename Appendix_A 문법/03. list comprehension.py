# list comprehension :: 리스트 컴프리헨션 : 리스트를 초기화 하는 방법중 하나
## 대괄호 안에  조건문, 반복문 넣는 방식으로 리스트를 초기화 가능.
# 한줄의 소스코드로 가능

# 0~19 까지 수중 홀수만 포함하는 리스트
array = [i for i in range(0,20) if i % 2 == 1]
print(array)


array = [i * i for i in range(0,20) if i % 2 == 1]
print(array)

# 2차원 리스트 초기화 할떄
n = 3
m =4
array = [[0] * m for _ in range(0,n)]
print(array)

## "_" ?? 언더바 UnderBar
#  단 순 반복수행시 변수값 무시 하고자할떄 언더바 사용,

summary =0
for i in range(1, 10):
    summary += i
print(summary)

for _ in range(1, 10):
    print("hello world")
