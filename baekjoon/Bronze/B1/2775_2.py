def recursion(n):
    global ho
    if n%ho and ho <= n:
        return recursion(n-1) + recursion(n - ho)
    else:
        return apart[n]

tc = int(input())

for t in range(1, tc+1):
    floor = int(input())
    ho = int(input())
    realFloor = floor+1
    apart = list(range(1, ho+1)) * realFloor

    result = recursion(realFloor*ho - 1)
    print(result)