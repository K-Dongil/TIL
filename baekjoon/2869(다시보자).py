import sys
A, B, V = map(int, sys.stdin.readline().split())
if (V-B)%(A-B) == 0:
    print((V-B)//(A-B))
else:
    print((V-B)//(A-B)+1)

#=====================================================
# import sys
# A, B, V = map(int, sys.stdin.readline().split())
# def snail(A, B, V):
#     result_day = 0
#     if (V-B)%(A-B) == 0:
#         result_day = (V-B)//(A-B)
#     else:
#         result_day = (V-B)//(A-B)+1
#     return result_day
# print(snail(A, B, V))


#V - A*x +B*(x-1) <= 0 ----------> (V-B)/(A-B) <=x
#=================================================================
# import sys
# afternoon, night, height = map(int, sys.stdin.readline().split())
# def snail(afternoon, night, height):
#     day = 0
#     while True:
#         height -= afternoon
#         day +=1
#         if height <=0:
#             break
#         height += night
#     return day
# print(snail(afternoon, night, height))