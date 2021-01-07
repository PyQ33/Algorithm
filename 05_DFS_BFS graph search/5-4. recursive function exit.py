import time

def recursive_function(i):
    if i == 123:
        return
        # 함수는 return 만나면 종료됨
    else:
        print(f'{i} 번쨰 재귀함수에서, {i+1}번째 재귀함수를 호출함')
        recursive_function(i+1)
        print(f'{i} 번쨰 재귀함수를 close')
        time.sleep(0.1)

recursive_function(1)