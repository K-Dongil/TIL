from collections import deque # 시간초과 해결

cardNum = int(input())
cards = deque(list(range(1, cardNum+1)))

while len(cards) != 1:
    cards.pop()
    cards.append(cards.pop())

print(cards[0])