data = [0, 4, 1, 3, 1, 2, 4, 1]

M = 5 # 0 ~ 4, data 개수가 아닌 data원소의 범위
N = len(data)
counts = [0] * M
temp = [0] * N

# 데이터가 각 항목별로 몇개 있는지 센다
for d in data:
    counts[d] += 1

# 정렬했을 때 각 숫자(data)의 앞에 위치할 data 개수를 반영하기 위해 counts의 원소를 조정
for i in range(M-1):
    counts[i+1] = counts[i] + counts[i+1]

for j in range(N-1, -1, -1):
    p = counts[data[j]] - 1
    temp[p] = data[j]
    counts[data[j]] -= 1
    # p1 = data[j] # j=7, p1=1
    # p2 = counts[p1] - 1 # p2 =3
    # temp[p2] = p1
    # counts[p1] -= 1

print(counts)
print(temp)