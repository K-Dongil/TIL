def normal(a, b, c):
    if not ((c < b and a < b) or (b < a and b < c)):
        result.append(b)

tc = int(input())

for t in range(tc):
    N = int(input())
    num_lst = list(map(int, input().split()))
    result = []

    for i in range(1, len(num_lst)-1):
        normal(num_lst[i-1], num_lst[i], num_lst[i+1])
    
    print(f'#{t+1} {len(result)}')