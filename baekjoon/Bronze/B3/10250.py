tc = int(input())

for t in range(tc):
    height, weight, nGuest = map(int, input().split())
    floor = 0
    ho = 0

    if nGuest % height:
        floor = nGuest % height
        ho = nGuest // height + 1
    else:
        floor = height
        ho = nGuest // height

    result = floor * 100 + ho
    print(result)