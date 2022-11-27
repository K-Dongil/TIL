def push(v):
    st.append(v)

def pop():
    if len(st):
        return str(st.pop(-1))
    return '-1'

def size():
    return str(len(st))

def empty():
    if len(st):
        return '0'
    return '1'

def top():
    if len(st):
        return str(st[-1])
    return '-1'

commandNum = int(input())
commands = [input().split() for _ in range (commandNum)]
st = []
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