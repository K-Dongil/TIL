N = int(input())
result = 0
st = []
while 0 < N:
    N -= 1
    nowV = int(input())
    if nowV == 0:
        wrongV = st.pop()
        result -= wrongV
    else:
        st.append(nowV)
        result += nowV

print(result)