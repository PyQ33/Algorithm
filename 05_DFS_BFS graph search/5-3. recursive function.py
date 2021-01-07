# 재귀함수  recursive function
import time

def recursive_function():
    print(f'this is {time.time()}')
    time.sleep(1)
    recursive_function()


recursive_function()