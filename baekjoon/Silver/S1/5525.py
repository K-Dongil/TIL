N = int(input())
experimentalLength = int(input())
experimentalStr = input()
controlStr = 'IO' * N + 'I'
cnt = 0

for i in range(experimentalLength - 2*N-1):
    for j in range(2*N+1):
        if experimentalStr[i+j] != controlStr[j]:
            break
    else:
        cnt += 1

print(cnt)