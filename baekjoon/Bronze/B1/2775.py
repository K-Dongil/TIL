tc = int(input())

for t in range(1, tc+1):
    floor = int(input())
    ho = int(input())
    apart = [list(range(1, ho+1)) for _ in range(floor+1)]

    for i in range(1, floor+1):
        for j in range(1, ho):
            apart[i][j] = apart[i][j-1] + apart[i-1][j]
    
    print(apart[floor][ho-1])