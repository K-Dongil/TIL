def push(n):
    s.append(n)

def pop():
    if len(s) == 0:
        return -1
    return s.pop(-1)


s = []

for i in range(5):
    push(i)

print(s)

for i in range(3):
    print(pop())
print(s)