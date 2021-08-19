def push(str):
    st.append(str)

def pop():
    if len(st) == 0:
        return 'Error'
    return st.pop(-1)

tc = int(input())
for t in range(tc):
    input_str = input()
    st = []
    result = 0

    for s in input_str:
        if s =='(' or s == '{' or s == '[':
            push(s)
        elif s ==')' or s == '}' or s == ']':
            parentheses = pop()
            if s ==')' and parentheses == '(':
                result = 1
            elif s =='}' and parentheses == '{':
                result = 1
            elif s ==']' and parentheses == '[':
                result = 1
            else:
                result = 0
                break # 틀렸을 때 바로 break를 주지 않으면 testcase가 {){}인 경우에 괄호가 올바르다고 나온다

    if len(st) != 0:
        result = 0

    print('#{} {}'.format(t+1, result))

#확인 해볼 testcase
#(()
#({)
#()}
#()})
#({)}
