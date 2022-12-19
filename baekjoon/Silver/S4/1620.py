import sys
input = sys.stdin.readline

pocketNum, questionNum = map(int, input().split())
pocketDict = {}

for i in range(1, pocketNum+1):
    pocketmon = input().strip()
    pocketDict[pocketmon] = i
    pocketDict[i] = pocketmon

for _ in range(questionNum):
    question = input().strip()
    try:
        print(pocketDict[int(question)])
    except:
        print(pocketDict[question])
