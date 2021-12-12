def selectionS(lst):
    N = len(lst)
    for i in range(N-1):
        minP = i
        for j in range(i+1, N):
            if lst[minP][1] > lst[j][1]:
                minP = j

        lst[minP], lst[i] = lst[i], lst[minP]

tc = int(input())

for t in range(1, tc+1):
    N = int(input())
    works = [list(map(int, input().split())) for _ in range(N)]
    selectionS(works)
    start = works[0][0]
    end = works[0][1]
    count = 1

    for work_start, work_end in works:
        if end <= work_start:
            count += 1
            start = work_start
            end = work_end

    print(f'#{t} {count}')