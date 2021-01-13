# dict
data = dict()
data['사과'] = 'apple'
data['바나나'] = 'banana'
data['딹기'] = 'strawberry'

print(data['바나나'])
print(data)

if '딹기' in data:
    print('"사과"in data set')

key_list = data.keys()
value_list = data.values()
print(key_list)
print(value_list)

print('---------key list -----------')
for key in key_list:
    print(data[key])


print('---------집합자료형 초기화-----------')
data = set([1,1, 2,3,4,4,5])
print(data)

data = {1,1,2,3,4,4,5}
print(data)

print('-----dict 연산-----')
a = set([1,1, 2,3])
b = set([3,4, 5,6])
print(a,b)
print(f"a|b : 합집합 {a|b}")
print(f"a&b : 교집합 {a&b}")
print(f"a-b : 차집합 {a-b}")
print(f"b-a : 차집합 {b-a}")

print('-----dict Function-----')

data = set([1,2,3,4])
print(data)

data.add(5)
print(data)

data.update([7,8,9,10])
print(data)

data.remove([3][0])
print(data)