tc = int(input())

for t in range(1, tc+1):
    st = list(map(str, input()))
    lst = []

    for i in range(len(st)):
        lastIn = st.pop()
        if len(lst) == 0:
            lst.append(lastIn)
        elif lst[-1] != lastIn:
            lst.append(lastIn)
        elif lst[-1] == lastIn:
            lst.pop()
    
    print('#{} {}'.format(t, len(lst)))