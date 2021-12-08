tc = int(input())

for t in range(1, tc+1):
    A, B = map(int, input().split())
    multiplication = -1
    if not (10 <= A or 10 <= B):
        multiplication = A * B
    
    print(f'#{t} {multiplication}')