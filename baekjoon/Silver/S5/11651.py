import sys
N = int(sys.stdin.readline())
coordinates = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
coordinates.sort(key= lambda x: (x[1], x[0]))

for coordinate in coordinates:
    print(coordinate[0], coordinate[1])
