def push(v):
    queue.append(v)

def pop():
    if len(queue):
        return str(queue.pop(0))
    return '-1'

def size():
    return str(len(queue))

def empty():
    if len(queue):
        return '0'
    return '1'

def front():
    if len(queue):
        return str(queue[0])
    return '-1'

def back():
    if len(queue):
        return str(queue[-1])
    return '-1'

commandNum = int(input())
commands = [input().split() for _ in range (commandNum)]
queue = []
result = ''

for command in commands:
    if command[0] == 'push':
        push(command[1])
    elif command[0] == 'pop':
        result += pop() + '\n'
    elif command[0] == 'size':
        result += size() + '\n'
    elif command[0] == 'empty':
        result += empty() + '\n'
    elif command[0] == 'front':
        result += front() + '\n'
    elif command[0] == 'back':
        result += back() + '\n'

print(result)