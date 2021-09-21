# 2 9889일 때 testcase 틀린 부분이 있었다.
import sys
sys.stdin = open("1493_input.txt", "r")

def find_position(p):
    x = 1
    y = 1
    sum = 0
    for i in range(1, p+1):
        sum += i
        if p == sum:
            y = 1
            x = i
            break
        elif p < sum:
            y = i
            x = 1
            sum = sum - i +1
            p = p - sum
            for j in range(p):
                x += 1
                y -= 1
            break
    return x, y


def find_dot(x, y):
    dot = 0
    while x != 1:
        dot += 1
        x -= 1
        y += 1
    dot += 1
    for i in range(1, y):
        dot += i
    return dot


tc = int(input())

for t in range(tc):
    x, y = map(int, input().split())
    new_position1 = find_position(x)
    new_position2 = find_position(y)
    x = new_position1[0] + new_position2[0]
    y = new_position1[1] + new_position2[1]
    dot = find_dot(x,y)

    print(f'#{t+1} {dot}')