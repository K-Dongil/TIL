n = int(input())
idx = 0
nowV = 1

while nowV < 1000000000:
    idx += 1
    nowV += 6 * idx
    if n <= nowV:
        break

print(idx+1 if n != 1 else 1)