import sys
C = int(input())
for i in range(C):
    totalScore = 0
    highStudent = 0
    avg_score = 0
    a = list(map(int, sys.stdin.readline().split()))
    for j in range(1, len(a)):
        totalScore += a[j]
        if j == len(a)-1:
            avg_score = totalScore/(len(a)-1)
    else:
        for k in range(1, len(a)):
            if a[k] > avg_score:
                highStudent += 1
        else:
            print('%0.3f' %(highStudent/a[0]*100) +'%')