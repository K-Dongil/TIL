now_x, now_y, right_up_x, right_up_y = map(int, input().split())
distance = []
distance.append(now_x - 0)
distance.append(right_up_x - now_x)
distance.append(now_y - 0)
distance.append(right_up_y - now_y)

print(min(distance))