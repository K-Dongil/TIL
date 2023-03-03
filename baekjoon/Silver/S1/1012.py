import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    for i in range(4):
        newX = x+dx[i]
        newY = y+dy[i]
        if 0<=newY<height and 0<=newX<width and farm[newY][newX] == 1:
            farm[newY][newX] = 0
            dfs(newX, newY)

dx = [0, 0 , 1, -1]
dy = [-1, 1, 0, 0]

T = int(input())

for t in range(T):
    width, height, vegetableNum = map(int, input().split())
    farm = [[0]*width for _ in range(height)]
    result = 0

    for i in range(vegetableNum):
        x, y = map(int, input().split())
        farm[y][x] = 1
    
    for x in range(width):
        for y in range(height):
            if farm[y][x] == 1:
                dfs(x, y)
                result += 1
    
    print(result)