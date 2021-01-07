# 어떤수를 1이 될때까지 나누기, 홀수일땐 1을 뺀 후 계속 할떄, 몇번 연산하나?

n , k = map(int, input().split())
result = 0

# n  > k : / k
while n >= k:
    ## 탈출조건, n이 k로 나누어떨어지지 않는다면 1씩빼기
    while n % k != 0: # 나누기 한게 0 이 아니면
        n -= 1
        result += 1
        print(f" n : {n} , \n 에서 빼기 1하는중 ...{result}회차")
    # 그 외의 경우 k 로 나누기
    n //= k
    result += 1
    print(f" n : {n} , \n 에서 나누기 k : {k}하는중 ...{result}회차")

# 마지막 남은 수에 1씩 빼기 == k - 2
while n > 1:
    n -= 1
    result += 1
    print(f' n : {n} , \n 에서 뺴기 1하는중 ...{result} 회차')

print(result)