T = int(input())

for i in range(T):
    long_str = input()

    count = 0
    lst = []
    for j in long_str:
        a = long_str.count(j)
        lst.append(a)
    print(f'#{i+1} {min(lst)-1}')