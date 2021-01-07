# 입력예시 : N, M , K
# N 개의 총 자연수, M 번 더해서 가장큰수만들기, K 번을 초과해서 연속더하기는 안됨
# == 가장큰것   K 번까지 연속해서 더하기, 두번쨰로 큰것 붙인후, 다시 가장큰것  K 번 더하기
# 입력예시 : 5, 8, 3
# 데이터  2, 4, 5, 4, 6
# 출력예시 : 46

input_line1 = "5 8 3"
input_line2 = "2 4 5 4 6"

# n, m, k 를 공백으로 구분해서 입력받기
# n, m, k = map(int, input().split())
n, m, k = map(int, input_line1.split())
print(f" n : {n},\n m :{m} , \n k : {k} ")


# N 개 수를 공백으로 구분하여 입력받기
# data = list(map(int, input().split()))
data = list(map(int, input_line2.split()))
print(f" data : {data}")


data.sort() # let  오름차순 갈수록 커지게
print(data)
first = data[n-1] #Larger
second = data[n-2] # Second

print(first, second)

# 큰수만들기
result = 0

# count : first 가 더해지는 수 계산 (수학)
count = int(m // (k+1)) * k
count += m % (k+1)

result += (count) * first
result += (m-count) * second

print(result)