## queue 는 라이브러리쓰자
from collections import deque

queue = deque()

queue.append(5)
queue.append(15)
queue.append(25)
queue.append(35)
queue.popleft() ## firt in first out
print(queue)
queue.append(45)
queue.append(25)
queue.append(55)
queue.append(65)
queue.popleft()
queue.append(35)
print(queue)

queue.reverse()
print(queue)
