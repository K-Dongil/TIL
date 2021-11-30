tc = int(input())

for t in range(1, tc+1):
    inputBit = input()
    bitLen = len(inputBit)
    originalBit = [False] * bitLen
    for i in range(bitLen):
        if inputBit[i] == '1':
            originalBit[i] = True
    nowBit = [False] * bitLen
    change = 0

    for i in range(bitLen):
        if originalBit[i] != nowBit[i]:
            coverBit = not nowBit[i]
            change += 1
            for j in range(i, bitLen):
                nowBit[j] = coverBit

        if originalBit == nowBit:
            break

    print(f'#{t} {change}')