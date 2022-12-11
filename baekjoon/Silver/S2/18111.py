vertical, width, inventory = map(int, input().split())
lands = [list(map(int, input().split())) for _ in range(vertical)]
minHeight = min([min(land) for land in lands])
maxHeight = max([max(land) for land in lands])
sec = 500*500*257*2
height = 0

for targetHeight in range(minHeight, maxHeight+1):
    useBlock = 0
    putBlock = 0
    nowSec = 0

    for land in lands:
        for nowHeight in land:
            if nowHeight < targetHeight:
                useBlock += targetHeight - nowHeight
            elif nowHeight > targetHeight:
                putBlock += nowHeight - targetHeight
    
    if putBlock + inventory < useBlock:
        continue
    
    nowSec = useBlock + 2*putBlock

    if nowSec <= sec:
        sec = nowSec
        height = targetHeight
    else:
        break

    
print(sec, height)