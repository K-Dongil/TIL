def binary(target):
    left = 0
    right = num1 - 1
    while left <= right:
        middle = (left + right) // 2

        if numList1[middle] > target:
            right = middle - 1
        elif numList1[middle] < target:
            left = middle + 1
        else: 
            return '1' + '\n'
    return '0' + '\n'


num1 = int(input())
numList1 = sorted(list(map(int, input().split())))
num2 = int(input())
numList2 = list(map(int, input().split()))
result = ''

for num in numList2:
    result += binary(num)

print(result)