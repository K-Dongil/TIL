coordinateNum = int(input())
coordinates = [list(map(int, input().split())) for _ in range(coordinateNum)]
coordinates.sort(key=(lambda x: (x[0], x[1])))
result = ''

for coordinate in coordinates:
    result += str(coordinate[0]) + ' ' + str(coordinate[1]) + '\n'
    
print(result)