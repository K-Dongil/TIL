N = int(input())
wantSequence = [int(input()) for _ in range(N)]
makeSequence = []
st = []
idx = 0
result = ''

for i in range(1, N+1):
    st.append(i)
    makeSequence.append('+')
    if len(st) != 0 and st[-1] == wantSequence[idx]:
        st.pop()
        makeSequence.append('-')
        idx += 1
        x = True

        while x:
            if len(st) == 0:
                break
            if st[-1] == wantSequence[idx]:
                st.pop()
                makeSequence.append('-')
                idx += 1
            else:
                x = False

if N == idx:
    for l in makeSequence:
        result += l + '\n'
else:
    result = 'NO'

print(result)