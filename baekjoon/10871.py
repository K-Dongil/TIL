import sys
N, X = map(int, input().split())
for i in range(N):
    A = map(int, sys.stdin.readline().split())
    if X > A:
        print(A+' \0')