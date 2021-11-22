def powerset(k):
    if k == len(str1):
        a = ''
        for i in range(len(t)):
            if t[i]:
                a += str1_lst[i]
        result1.append(a)

    else:
        t[k] = True
        powerset(k+1)
        t[k] = False
        powerset(k+1)

def powerset1(k):
    global c
    if k == len(str2):
        b = ''
        for i in range(len(t)):
            if t[i]:
                b += str2_lst[i]
        if b in result1:
            if c < len(b):
                c = len(b)


    else:
        t[k] = True
        powerset1(k+1)
        t[k] = False
        powerset1(k+1)

tc = int(input())

for TC in range(1, tc+1):
    str1, str2 = input().split()
    str1_lst = list(str1)
    str2_lst = list(str2)
    t = [False] * len(str1)
    result1 = []
    result2 = []
    c = 0

    powerset(0)
    print(result1)
    t = [False] * len(str2)
    powerset1(0)
 
    print(f'#{TC} {c}')