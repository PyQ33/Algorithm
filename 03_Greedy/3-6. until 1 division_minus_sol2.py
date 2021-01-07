# 어떤수를 1이 될때까지 나누기, 홀수일땐 1을 뺀 후 계속 할떄, 몇번 연산하나?

n , k = map(int, input().split())
result = 0

# n  > k : / k
while True:
    # n 나누기 몫 k , 곱하기 몫 : 나머지 외의 숫자 가 target
    target = (n//k) * k
    print(target)

    target = round(n - n%k, 0)
    print(target)

    result += (n- target)  # result 에 빼기 1 하는 횟수 계산해서 넣음
    n = target

    # 반복문 탈출
    if n < k:
        break

    # k 로 나누기
    result += 1
    n //= k
    print(f' n : {n} , \n 에서 뺴기 1하는중 ...{result} 회차')

    # n = n // k : 다음 n은 n을 k 로 나눈 몫

result += n- 1

print(result)