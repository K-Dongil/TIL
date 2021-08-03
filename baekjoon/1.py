N = int(input())
result = N//5
N %= 5
result += N//3
N %= 3
if N:
    result = -1
print(result)