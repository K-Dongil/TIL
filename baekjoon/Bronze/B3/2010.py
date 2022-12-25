import sys

multiTap = int(sys.stdin.readline())
maxPlugs = [int(sys.stdin.readline()) for _ in range(multiTap)]
result = sum(maxPlugs) - multiTap + 1

print(result)