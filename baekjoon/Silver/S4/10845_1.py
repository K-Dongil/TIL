def push(v):
    global nowIdx
    queue[nowIdx] = v
    nowIdx += 1

def pop():
    global nowIdx
    if nowIdx:
        firstV = queue[nowIdx]
        queue[nowIdx] = 0
        nowIdx -= 1
        return str(firstV)
    return '-1'

def size():
    return str(nowIdx)

def empty():
    if nowIdx:
        return '0'
    return '1'

def front():
    if nowIdx:
        return str(queue[0])
    return '-1'

def back():
    if nowIdx:
        return str(queue[-1])
    return '-1'

commandNum = int(input())
commands = [input().split() for _ in range (commandNum)]
queue = [0] * commandNum
nowIdx = 0
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