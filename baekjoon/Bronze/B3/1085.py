now_x, now_y, right_up_x, right_up_y = map(int, input().split())
distance = []
distance.append(now_x - 0)
distance.append(right_up_x - now_x)
distance.append(now_y - 0)
distance.append(right_up_y - now_y)

print(min(distance))

##############################################################
now_x, now_y, right_up_x, right_up_y = map(int, input().split())
min_distance = right_up_x + right_up_y
if now_x < min_distance:
    min_distance = now_x
if right_up_x - now_x < min_distance:
    min_distance = right_up_x - now_x
if now_y < min_distance:
    min_distance = now_y
if right_up_y - now_y < min_distance:
    min_distance = right_up_y -now_y

print(min_distance)