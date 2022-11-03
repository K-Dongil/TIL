keepLine, needLine = map(int, input().split())
keepLineList = [int(input()) for _ in range(keepLine)]
maxLineLen = 0
left = 1
right = max(keepLineList)
#visited = [False] * right # 배열 활용시 메모리 초과

while left <= right:
    cnt = 0
    middle = (left+right) // 2

    for l in keepLineList:
        cnt += l // middle
    
    if needLine <= cnt:
        maxLineLen = middle
        left = middle + 1 # 잘라진 랜선 개수가 요구사항을 만족하면 mid 밑으로는 볼 필요 x
    elif cnt < needLine:
        right = middle - 1 # 잘라진 랜선 개수가 요구사항을 불만족시키면 mid 위로는 볼 필요 x

print(maxLineLen)