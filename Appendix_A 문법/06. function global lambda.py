#
def add(a,b):
    print(f"result is {a / b}")

add(b=5, a=3)
print('----------------------')
a = 0
def func():
    a = 0
    #global a
    a +=1

for i in range(0,10):
    func()

print(a)
print('-------global in def-----------')
a = 0
def func():
    global a
    a +=1

for i in range(0,10):
    func()

print(a)

print('-------labmda function----------')

def add(a,b):
    return a +b

print(add(3,7))
print((lambda  a, b : a+b)(3,9))