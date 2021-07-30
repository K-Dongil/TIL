testcase = int(input())
for i in range(testcase):
    nums = list(map(int, input().split()))
    sum_num = 0
    for num in nums:
        if num % 2:
            sum_num += num
    print('#{} {}'.format(i+1, sum_num))

#=======================================================
# import sys
# testcase = int(input())
# for i in range(testcase):
#     nums = list(map(int, sys.stdin.readline().split()))
#     sum_num = 0
#     for num in nums:
#         if num % 2:
#             sum_num += num
#     print('#{} {}'.format(i+1, sum_num))