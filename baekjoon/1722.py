def permutation(k):
    if k == len(num_lst):
        results.append(' '.join(p))
        return
    else:
        for i in range(len(num_lst)):
            if not visited[i]:
                visited[i] = True
                p[k] = num_lst[i]
                permutation(k+1)
                visited[i] = False 

n = int(input())
num_lst = list(range(1, n+1))
for i in range(len(num_lst)):
    num_lst[i] = str(num_lst[i])
    
lst = input().split()
k = lst[0]
visited = [False] * n
p = [0] * n
results = []

permutation(0)

if k == '1':
    num = int(lst[1])
    print(results[num-1])
elif k == '2':
    num = ' '.join(lst[1:])
    for i in range(n):
        if num == results[i]:
            print(i+1)