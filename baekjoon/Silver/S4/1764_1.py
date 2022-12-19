import sys
input = sys.stdin.readline

listen, see = map(int, input().split())
total = listen + see
record = {}
guests = []

for i in range(total):
    name = input().strip()
    if record.get(name) is None:
        record[name] = True
    else:
        guests.append(name)

print(len(guests))
guests.sort()

for guest in guests:
    print(guest)