def per(k):
    if k==3:
        for i in range(3):
            # pos = t[i]
            # print(a[pos], end= ' ')
            print(a[t[i]], end=' ')
        print()
    else:
        for i in range(3):
            if not visited[i]: # 사용 안한 경우에
                t[k] = i
                visited[i] = True
                per(k+1)
                visited[i] = False

a = [20, 31, 78]
# 0, 1, 2 => 20, 31, 78
# 0, 2, 1 => 20, 78, 31
# 1, 0, 2 => 31, 20, 78
# 1, 2, 0 => 31, 78, 20
# 2, 0, 1 => 78, 31, 20
# 2, 1, 0 => 78, 20, 31

t = [-1] * len(a)
visited = [False] * len(a)
per(0)
