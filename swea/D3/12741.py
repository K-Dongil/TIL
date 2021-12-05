tc = int(input())

for t in range(1, tc+1):
    start_x, end_x, start_y, end_y = map(int, input().split())
    overlap_start = 0
    overlap_end = 0
    time = 0
    if start_x < start_y and 