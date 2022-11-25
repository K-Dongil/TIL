def dp(n):
    global ho
    if n%ho == 0 or n < ho:
        return apart[n]
    if apart[n] not in list(range(1, ho+1)):
        return apart[n]
    apart[n] = dp(n-1) + dp(n - ho)
    return apart[n]

tc = int(input())

for t in range(1, tc+1):
    floor = int(input())
    ho = int(input())
    realFloor = floor+1
    apart = list(range(1, ho+1)) * realFloor

    result = dp(realFloor*ho - 1)
    print(result)