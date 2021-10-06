a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
t = [False] * 10

def powerset(k, s):
    if k == 10:
        if s == 10:
            print(t, end= ' ')
            for i in range(len(t)):
                if t[i]:
                    print(a[i], end=' ')
            print()

    else:
        for i in range(2):
            t[k] = i
            
            if t[k]:
                s += a[k]
                if s > 10:
                    return

            powerset(k+1, s)

powerset(0, 0)