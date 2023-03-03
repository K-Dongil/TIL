def solve(x, y):
    for i in range(4):
        newX = x+dx[i]
        newY = y+dy[i]
        if (newX, newY) in pesticide:
            pesticide.remove((newX,newY))
            solve(newX, newY)

dx = [0, 0 , 1, -1]
dy = [-1, 1, 0, 0]

T = int(input())

for t in range(T):
    width, height, vegetableNum = map(int, input().split())
    pesticide = []
    result = 0

    for i in range(vegetableNum):
        x, y = map(int, input().split())
        pesticide.append((x, y))
    
    for x, y in pesticide:
        pesticide.remove((x,y))
        solve(x, y)
        result += 1

    print(result)