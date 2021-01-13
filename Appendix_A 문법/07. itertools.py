# itertools : 파이썬에서 반복 데이터 처리하는 기능.
# permutations, combinations 순열 조합

from itertools import permutations
from itertools import combinations
from itertools import product
from itertools import combinations_with_replacement



data = ['A','B','C']

result = list(permutations(data,3))  # 모든 순열 구하기
print(result)

result = list(permutations(data,2))  # 모든 순열 구하기
print(result)

result = list(combinations(data,3))  # 모든 조합 구하기
print(result)

result = list(product(data,repeat=2))  # 모든 중복순열 구하기
print(result)

result = list(combinations_with_replacement(data,2))  # 모든 중복조합 구하기
print(result)
