
input_line1 = "3 3"
input_line2 = "3 1 2"
input_line3 = "4 1 4"
input_line4 = "2 2 2"
input_list = [input_line2, input_line3, input_line4]


# n, m, k 를 공백으로 구분해서 입력받기
# n, m, k = map(int, input().split())
n, m = map(int, input_line1.split())
print(f" n : {n},\n m : {m} , \n")

result = 0

# 한 줄씩 입력받기
for i in input_list:
    data = list(map(int, i.split()))
    print(data)
    min_value = min(data)
    result = max(result, min_value) # 이전의 result 와 지금의  minvalue 비교,
    # 더큰 minvalue 있을경우  result 를 갱신,
print(result)