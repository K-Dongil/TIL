lst = [7, 4, 2, 0, 0, 6, 0, 7, 0]
max_v = lst[0]
result = 0

for i in range(len(lst)):
    count = 0

    for j in range(i+1, len(lst)):
        if lst[i] > lst[j]:
            count += 1

    if result < count:
        result = count

print(result)