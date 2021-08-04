def checkNum(a): # 인자로 보낸 값이 한수인지 아닌지 판별하는 함수
    gapList = [] # gapList는 각 자리의 값으로 채워질 리스트
    gapList1 = [] # gapList1는 연속된 두개의 수 차이들로 채워질 리스트

    strNum = str(a) # 각 자리의 수를 서로 비교하기 위해 int형으로 받은 값을  문자형 변환한다. 
    if len(strNum) ==1 or len(strNum) ==2 : # 1 ~ 99 까지의 수는 모두 한수이므로
        return a # 인자로 보낸값을 그대로 반환

    for i in range(len(strNum)): # 입력받은 자리의 크기만큼 (1의자리, 10의자리 , 100의자리) for문을 반복한다 
        gapList.append(strNum[i]) # 숫자의 각 자리들을 큰 자리의 수부터 gapList에 채워 넣는다

    for i in range((len(gapList))-1): # gapList에 담긴 각 자리의 수를 이용하여 연속된 두 수의 차를 구하기 위해 gapList의 길이보다 1짧게 for문을 돌린다
        gapList1.append((int(gapList[i]) - int(gapList[i+1]))) # 연속된 두수의 차를 구해 gapList1에 추가

    for i in range(len(gapList1)-1): # gapList1에는 연속된 두개의 수 차이들이 담겨져 있다
        if gapList1[i] == gapList1[i+1]: # 연속된 두개의 수 차이가 같다면
            pass # 통과
        else: # 연속된 두개의 수 차이가 다르다면
            a = None #반환값이 될 a에 None 값을 집어넣고
            break # for문을 멈춘다
    return a # 한수라면 받은 인자값을 그대로 돌려주고 아니라면 None값 반환

N = int(input()) # 숫자 N을 입력받는다
numList = [] # 한수들을 담을 List

for i in range(1, N+1): # 입력받은 숫자 N만큼 1부터 차례대로 임시변수 i에 담아 
    numList.append(checkNum(i)) # 한수인지 아닌지 check해주는 함수에 값을 보내 결과값을 받아 리스트에 추가한다
numSet = set(numList) # 한수가 아닐때는 함수가 None값을 보내므로 set을 이용하여
if None in numSet: # 남아잇는 None값을 제거
    numSet.remove(None)
print(len(numSet)) # numSet에는 한수값들만 남아있으므로 길이를 구하여 출력

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
# NumList = []

# for i in numList:
#     NumList.append(removeNum(i))
# numSet = set(NumList)
# if None in numSet:
#     numSet.remove(None)
# print(len(numSet))