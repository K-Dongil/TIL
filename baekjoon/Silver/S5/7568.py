peopleNum = int(input())
peoples = [list(map(int, input().split())) for _ in range(peopleNum)]
result = ''

for i in range(peopleNum):
    rank = 1
    for j in range(peopleNum):
        if peoples[i][0] < peoples[j][0] and peoples[i][1] < peoples[j][1]:
            rank += 1
    result += str(rank) + ' '

print(result)