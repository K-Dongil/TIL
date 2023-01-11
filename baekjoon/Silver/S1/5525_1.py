N = int(input())
experimentalLength = int(input())
experimentalStr = input()
controlStr = 'IO' * N + 'I'
skip = [0] * 128
idx = 0
limitIdx = experimentalLength - 2*N -1
cnt = 0

for i in range(2*N+1):
    skip[ord(controlStr[i])] = 2*N+1 - i -1

while idx <= limitIdx:
    for i in range(2*N, -1, -1):
        if experimentalStr[idx+i] != controlStr[i]:
            if experimentalStr[idx+i] in controlStr:
                idx += max(1, skip[ord(experimentalStr[idx+i])])
            else:
                idx += i if 0 < i else 1
            break
    else:
        idx += 2
        cnt += 1

print(cnt)