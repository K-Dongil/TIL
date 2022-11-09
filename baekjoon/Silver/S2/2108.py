N = int(input())
numbers = sorted([int(input()) for _ in range(N)])
average = 0
middle = numbers[N//2] #  if 2 < N else numbers[0]
cntDict = {number: 0 for number in numbers}
maxV = -4000
minV = 4000
modeCnt = 0
modes = []

for number in numbers:
    average += number
    cntDict[number] += 1
    if number < minV:
        minV = number
    if maxV < number:
        maxV = number

for value in cntDict.values():
    if modeCnt < value:
        modeCnt = value
for key, value in cntDict.items():
    if value == modeCnt:
        modes.append(key)
modes.sort()

average = round((average / N))

print(average)
print(middle)
print((modes[1] if 2 <= len(modes) else modes[0]) if 2 < N else maxV)
print(abs(maxV - minV))