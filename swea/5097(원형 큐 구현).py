# tc = int(input())
#
# for t in range(tc):
#     N, M = map(int, input().split())
#     lst = list(map(int, input().split()))
#
#     for i in range(M):
#         a = lst.pop(0)
#         lst.append(a)
#
#     print('#{} {}'.format(t+1, lst[0]))



# ======================================================================
# 원형큐 구현
def isEmpty():
	return front == rear

def isFull():
	return (rear+1) % len(q) == front

def enQueue(item):
	global rear
	if isFull():
		print("Queue_Full")
	else:
		rear = (rear + 1) % len(q)
		q[rear] = item

def deQueue():
	global front
	if isEmpty():
		print("Queue_Empty")
	else:
		front = (front + 1) % len(q)
		return q[front]

tc = int(input())

for t in range(tc):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    q = [0] * (N+1)

    front = 0
    rear = 0

    for i in range(len(lst)): # 큐에 데이터가 없어서
        enQueue(lst[i])

    for i in range(M):
        a = deQueue()
        enQueue(a)
        print(q)

    print('#{} {}'.format(t+1, q[(front + 1) % len(q)]))

