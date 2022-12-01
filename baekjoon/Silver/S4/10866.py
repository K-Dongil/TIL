def push_front(v):
    global startIdx
    deque[startIdx] = v
    startIdx -= 1

def push_back(v):
    global endIdx
    deque[endIdx] = v
    endIdx += 1

def pop_front():
    global startIdx
    if endIdx-startIdx-1:
        startIdx += 1
        firstV = deque[startIdx]
        deque[startIdx] = 0
        return str(firstV)
    return '-1'

def pop_back():
    global endIdx
    if endIdx-startIdx-1:
        endIdx -= 1
        endV = deque[endIdx]
        deque[endIdx] = 0
        return str(endV)
    return '-1'

def size():
    return str(endIdx-startIdx-1)

def empty():
    if endIdx-startIdx-1:
        return '0'
    return '1'

def front():
    if endIdx-startIdx-1:
        return str(deque[startIdx+1])
    return '-1'

def back():
    if endIdx-startIdx-1:
        return str(deque[endIdx-1])
    return '-1'

commandNum = int(input())
commands = [input().split() for _ in range (commandNum)]
deque = [0] * (2*commandNum)
endIdx = commandNum
startIdx = commandNum-1
result = ''

for command in commands:
    if command[0] == 'push_front':
        push_front(command[1])
    elif command[0] == 'push_back':
        push_back(command[1])
    elif command[0] == 'pop_front':
        result += pop_front() + '\n'
    elif command[0] == 'pop_back':
        result += pop_back() + '\n'
    elif command[0] == 'size':
        result += size() + '\n'
    elif command[0] == 'empty':
        result += empty() + '\n'
    elif command[0] == 'front':
        result += front() + '\n'
    elif command[0] == 'back':
        result += back() + '\n'

print(result)