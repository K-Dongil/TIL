tc = int(input())

for t in range(1, tc+1):
    inputStr = input()
    stackArea = []
    result = 1
    
    for s in inputStr:
        if s in ['(', '{']:
            stackArea.append(s)
        elif len(stackArea) == 0 and s in [')', '}']:
            result = 0
            break
        elif s == ')':
            lastInFirstOut = stackArea.pop()
            if lastInFirstOut != '(':
                result = 0
                break
        elif s == '}':
            lastInFirstOut = stackArea.pop()
            if lastInFirstOut != '{':
                result = 0
                break
    
    if len(stackArea):
        result = 0

    print('#{} {}'.format(t, result))