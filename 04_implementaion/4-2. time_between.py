# 00:00:00 시간 부터 ~ h:59:59 시간 사이의 모든시간중
# 3이 하나라도 포함되는 모든경우의수 를 구하는 프로그램 만들깅

#  h 입력받기
h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            # if per a time, isin 3, + count
            if '3' in str(i) + str(j) + str(k):
                count += 1
                # String.zfill(t자리수로) :: t자리수 문자열로, 숫자 앞에 0 채우기
                print(f"{str(i).zfill(2)}:{str(j).zfill(2)}:{str(k).zfill(2)}")
print(count)