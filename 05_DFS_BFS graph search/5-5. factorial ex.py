def factirial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def factorial_recursive(m):
    if m <= 1:
        return 1

    # n * (n-1)!
    return m * factorial_recursive(m-1)

print(f'iterative : {factirial_iterative(7)}')
print(f'recursive : {factorial_recursive(7)}')
