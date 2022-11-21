tc = int(input())

for t in range(tc):
    height, weight, nGuest = map(int, input().split())
    hotel = [[0]*weight for _ in range(height)]
    result = 0

    for i in range(weight):
        for j in range(height):
            nGuest -= 1
            if nGuest == 0:
                result = (j+1)*100 + (i+1)
                break
                
    print(result)

