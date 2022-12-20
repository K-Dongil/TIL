nowChannel = 100
finishChannel = input()
channelLen = len(finishChannel)
brokenButtonNum = int(input())
brokenButtons = list(map(int, input().split(' '))) if brokenButtonNum else []
notBrokenButtons = list(set(range(10)) - set(brokenButtons))
channels = []
goChannel = ''
leastPress = abs(int(finishChannel) - nowChannel)

for i in range(channelLen):
    if int(finishChannel[i]) not in brokenButtons:
        goChannel += finishChannel[i]
    else:
        if brokenButtonNum == 10:
            break
        leftChannel = goChannel
        rightChannel = goChannel
        left = int(finishChannel[i])-1
        right = int(finishChannel[i])+1

        while 0 <= left:
            if left in brokenButtons:
                left -= 1
            else:
                leftChannel += str(left)
                break

        while right <= 9:
            if right in brokenButtons:
                right += 1
            else:
                rightChannel += str(right)
                break

        leftChannel += str(notBrokenButtons[-1])*(channelLen-i-1)
        rightChannel += str(notBrokenButtons[0])*(channelLen-i-1)
        
        if len(leftChannel) == channelLen:
            channels.append(leftChannel)
        if len(rightChannel) == channelLen:
            channels.append(rightChannel)

        break
else:
    channels.append(goChannel)

for channel in channels:
    nowPress = abs(int(finishChannel) - int(channel)) + channelLen
    if nowPress < leastPress:
        leastPress = nowPress

print(leastPress)