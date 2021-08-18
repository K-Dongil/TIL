def fibo(n):
    table[0] = 0
    table[1] = 1

    for i in range(2, n+1):
        table[i] = table[i-1] + table[i-2]

    return table[n]

n = int(input())
table = [0] * (n+1)

print(fibo(n))