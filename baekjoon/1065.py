# def removeNum(a):
#     gapList = []
#     gapList1 = []
#     strNum = str(a)
#     if len(strNum) ==1:
#         return a
#     for i in range(len(strNum)):
#         gapList.append(strNum[i])
#     for i in range((len(gapList))-1):
#         gapList1.append((int(gapList[i]) - int(gapList[i+1])))
#     for i in range(len(gapList1)-1):
#         if gapList1[i] == gapList1[i+1]:
#             pass
#         else:
#             a = None
#             break
#     return a

# N = int(input()) # 숫자 N을 입력받는다

# numList = list(range(1, N+1))
# removeNumList = []

# for i in numList:
#     removeNumList.append(removeNum(i))
# setset = set(removeNumList)
# if None in setset:
#     setset.remove(None)
# print(len(setset))



def removeNum(a):
    gapList = []
    gapList1 = []

    strNum = str(a)
    if len(strNum) ==1 or len(strNum) ==2 :
        return a

    for i in range(len(strNum)):
        gapList.append(strNum[i])

    for i in range((len(gapList))-1):
        gapList1.append((int(gapList[i]) - int(gapList[i+1])))

    for i in range(len(gapList1)-1):
        if gapList1[i] == gapList1[i+1]:
            pass
        else:
            a = None
            break
    return a

N = int(input()) # 숫자 N을 입력받는다
removeNumList = []

for i in range(1, N+1):
    removeNumList.append(removeNum(i))
setset = set(removeNumList)
if None in setset:
    setset.remove(None)
print(len(setset))