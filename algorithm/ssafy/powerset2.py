def powerset(k, input, sumV):
    if sumV > 10:
        return

    if k == input:
        #print(t, end= ' ')
        # sumV = 0
        # for i in range(3):
        #     if t[i]:
        #         sumV += a[i]
        #         #print(a[i], end=' ')

        if sumV == 10:
            for i in range(3):
                if t[i]:
                    print(a[i], end=' ')
        print()
    else:
        t[k] = True
        powerset(k+1, input, sumV + a[k])
        t[k] = False
        powerset(k+1, input, sumV)
        # for i in range(2):
        #     t[k] = i
        #     powerset(k+1)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
t = [-1] * 10
powerset(0, 10, 0)