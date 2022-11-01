strNum = int(input())
strList = list(set([input() for _ in range(strNum)]))
listLen = len(strList)

#1 길이가 짧은 것부터
strDict = {}
for i in range(listLen):
    strDict[strList[i]] = len(strList[i])

for i in range(listLen):
    for j in range(i+1, listLen):
        if strDict[strList[j]] < strDict[strList[i]]:
            strList[i], strList[j] = strList[j], strList[i]

#2 길이가 같은 것일때 사전 순으로 정렬
for i in range(listLen-1):
    memory = strDict[strList[i]]
    for j in range(i+1, listLen):
        if memory != strDict[strList[j]]:
            break
        elif strList[j] < strList[i]:
            strList[i], strList[j] = strList[j], strList[i]

printStr = ''
for l in strList:
    printStr += l + '\n'

print(printStr)