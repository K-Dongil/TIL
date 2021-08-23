def f(i, N):
    if i == N: # 순열 완성된 상태
        print(P)
    else: # i번 원소값 결정
        for j in range(i, N): # 자신부터 오른쪽 원소와 교환
            P[i], P[j] = P[j], P[i]
            f(i+1, N)
            P[i], P[j] = P[j], P[i]

P = [1, 2, 3, 4, 5]
f(0, len(P))




def f1(i, N, r):
    if i == N: # 순열 완성된 상태
        print(P[0:r])
    else: # i번 원소값 결정
        for j in range(i, N): # 자신부터 오른쪽 원소와 교환
            P1[i], P1[j] = P1[j], P1[i]
            f1(i+1, N, r)
            P1[i], P1[j] = P1[j], P1[i]

P1= [1, 2, 3, 4, 5]
f1(0, len(P1), 3)