from collections import deque
people, order = map(int, input().split())
circleSit = deque(range(1, people+1))
Josephus = []
number = len(circleSit)
cnt = 0
result = '<'

while circleSit:
    nowPeople = circleSit.popleft()
    cnt += 1
    if cnt % order:
        circleSit.append(nowPeople)
    else:
        Josephus.append(nowPeople)

for i in range(people):
    if i == people-1:
        result += str(Josephus[i]) + '>'
    else:
        result += str(Josephus[i]) + ', '

print(result)