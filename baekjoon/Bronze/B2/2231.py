n = int(input())
lst = list(map(str, list(range(n//2, n))))
result = 0

for l in lst:
    decomposition = int(l)
    for s in l:
        decomposition += int(s)
    if decomposition == n:
        result = l
        break

print(result)