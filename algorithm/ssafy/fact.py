def fact(n):
    if n == 1:
        return n
    result = n*fact(n-1)
    return result

print(fact(5))