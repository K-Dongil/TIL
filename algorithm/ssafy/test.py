t = int(input())
for num in range(1, t + 1):
    arr = list(map(str, input()))
    result = []

    for i in range(len(arr)):
        if len(result) == 0:
            result.append(arr[i])
        elif arr[i] != result[-1]:
            result.append(arr[i])
        else:
            result.pop(-1)
    print(f'#{num} {(len(result))}')