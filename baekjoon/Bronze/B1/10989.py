import sys

N = int(input())
counts = [0]*10001
idx = 0

for i in range(N):
    num = int(sys.stdin.readline())
    counts[num] += 1

for count in counts:
    if 1 <= count:
        for i in range(count):
            print(idx)
    idx += 1

""" 계수정렬
N = int(input())
datas = [int(input()) for _ in range(N)]
counts = [0]*10001
sortList = [0] * N

for data in datas:
    counts[data] += 1

for i in range(10000):
    counts[i+1] = counts[i] + counts[i+1]

for i in range(N-1, -1, -1):
    nowV = counts[datas[i]] - 1
    sortList[nowV] = datas[i]
    counts[data[i]] -= 1

print(sortList)
"""