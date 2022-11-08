start, end = map(int, input().split())
decimal = list(range(2, end+1))
idx = 0
result = []

while idx < len(decimal):
    if decimal[idx]:
        if start <= decimal[idx]:
            result.append(decimal[idx])
        for i in range(idx, len(decimal), decimal[idx]):
            #print(decimal[i])
            decimal[i] = 0
            
    idx += 1

for l in result:
    print(l)