def push(v):
    global nowIdx
    st[nowIdx] = v
    nowIdx += 1

def pop():
    global nowIdx
    if nowIdx:
        nowIdx -= 1
        v = st[nowIdx]
        st[nowIdx] = 0
        return str(v)
    return '-1'

def size():
    global nowIdx
    return str(nowIdx)

def empty():
    global nowIdx
    if nowIdx:
        return '0'
    return '1'

def top():
    global nowIdx
    if nowIdx:
        return str(st[nowIdx-1])
    return '-1'

commandNum = int(input())
commands = [input().split() for _ in range (commandNum)]
st = [0] * 100000
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
    elif command[0] == 'top':
        result += top() + '\n'

print(result)