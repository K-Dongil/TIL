nMinNum = int(input())
num = 666
cnt = 0
result = 0

while True:
    if '666' in str(num):
        cnt += 1
        if cnt == nMinNum:
            result = num
            break
    num += 1

print(result)