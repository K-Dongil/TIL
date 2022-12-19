import sys
input = sys.stdin.readline

listen, see = map(int, input().split())
total = listen + see
record = {}
guests = []
result = 0

for i in range(total):
    name = input().strip()
    try:
        if record[name]:
            guests.append(name)
            result += 1
    except:
        record[name] = name

guests.sort()
print(result)

for guest in guests:
    print(guest)