tc = int(input())
result = [0] * tc

for i in range(tc):
    start_x, end_x, start_y, end_y = map(int, input().split())
    overlap_start = 0
    overlap_end = 0
    
    if start_x <= start_y and end_y <= end_x:
        overlap_start = start_y
        overlap_end = end_y
    elif start_x <= start_y and start_y <= end_x <= end_y:
        overlap_start = start_y
        overlap_end = end_x
    elif start_y <= start_x and end_x <= end_y:
        overlap_start = start_x
        overlap_end = end_x
    elif start_y <= start_x and start_x <= end_y <= end_x:
        overlap_start = start_x
        overlap_end = end_y

    time = overlap_end - overlap_start
    result[i] = time

for t in range(1, tc+1):
    print('#{} {}'.format(t, result[t-1]))