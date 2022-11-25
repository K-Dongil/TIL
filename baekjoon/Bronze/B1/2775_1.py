tc = int(input())

for t in range(1, tc+1):
    floor = int(input())
    ho = int(input())
    realFloor = floor+1
    apart = list(range(1, ho+1)) * realFloor

    for i in range(ho, realFloor*ho):
        if i % ho:
            apart[i] = apart[i-1] + apart[i-ho]

    print(apart[realFloor*ho -1])