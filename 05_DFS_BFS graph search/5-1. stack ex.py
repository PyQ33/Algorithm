stack = []

stack.append(5)
stack.append(2)
stack.append(52)
stack.append(4)
stack.append(15)
stack.pop() # 맨 마지막 들어간 녀석을 빼냄
print(stack)
stack.append(25)
stack.append(35)
stack.pop()

print(stack)
print(stack[::-1])
