tc = int(input())

for t in range(tc):
    a_triangle, b_triangle = map(int, input().split())

    print(f'#{t+1} {a_triangle**2//b_triangle**2}')