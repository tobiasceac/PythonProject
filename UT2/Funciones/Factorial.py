def factorial(n):
    if n <= 0:
        return -1

    result = 1
    for i in range(1, n + 1):
        print(i)
        result *= i

    return result

def factorialRecursive(n):
    if n <= 0:
        return -1
    else:
        return n * factorialRecursive(n - 1)

print(factorial(5))

print(factorialRecursive(-2))
