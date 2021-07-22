import sys
A, B, V = map(int, sys.stdin.readline().split())
def snail(A, B, V):
    day = V//(A-B)+1 if A-B !=1 else V//(A-B)-A+1
    return day
print(snail(A, B, V))
#V - A*x +B*x <= A
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