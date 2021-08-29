def circle_que(lst):
    front = 0
    rear = 0
    minus = 1
    q = [0] * 8
    for i in range(len(lst)):
        q[i] = lst[i]
    while q[-1] > 0:
        q.pop(0)
        front += 1
        q.append()





for t in range(10):
    tc = int(input())
    lst = list(map(int, input().split()))



# def abc(lst):
#     idx = 1
#     while lst[-1] > 0:
#         a = lst.pop(front)
#         lst.append(a - idx)
#         if idx == 5:
#             idx = 1
#             continue
#         idx += 1
#     lst.pop(-1)
#     lst.append(0)
#     return lst
# for t in range(10):
#     tc = int(input())
#     lst = list(map(int, input().split()))
#     lst = abc(lst)
#     print('#{} '.format(tc), end='')
#     print(*lst)


# test_cases = 10
#
# for t in range(1, test_cases + 1):
#     test_num = int(input())
#     queue = list(map(int, input().strip().split()))
#     front = 0
#     rear = len(queue) - 1
#     i = 0
#     while queue[rear] > 0:
#         queue[front] -= i + 1
#         i = (i + 1) % 5
#         front = (front + 1) % 8
#         rear = (rear + 1) % 8
#     queue[rear] = 0
#
#     print('#%d ' % t, end='')
#     while front != rear:
#         print('%d' % queue[front], end=' ')
#         front = (front + 1) % 8
#     print('%d' % queue[front])


for tc in range(1, 11):
    num = int(input())
    arr = list(map(int, input().split()))
    r = 1

    while r == 1:
        for i in range(1, 6):
            arr.append(arr.pop(0) - i)
            if arr[-1] <= 0:
                arr[-1] = 0
                r = 0
                break

    result = " ".join([str(_) for _ in arr])
    print(f'#{num} {result}')