import sys
N, X = map(int, input().split())
A = sys.stdin.readline().split()
for i in range(N):
    if X > int(A[i]):
        print(A[i], end=' ')