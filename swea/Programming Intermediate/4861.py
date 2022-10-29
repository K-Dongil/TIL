import sys
sys.stdin = open('4861_input.txt', 'r')

tc = int(input())

for t in range(tc):
    N, M = map(int, input().split())
    str_lst = [input() for _ in range(N)]

    for i in range(N):
        add_str =''
        for j in range(N):
            add_str += str_lst[j][i]
        str_lst.append(add_str)

    new_str_lst = []

    for i in str_lst:
        for j in range(len(i)-M+1):
            new_str_lst.append(i[j:j+M])

    for s in new_str_lst:
        new_str = ''
        for i in range(len(s)-1, -1, -1):
            new_str += s[i]
        if s == new_str and len(s) == M:
            print('#{} {}'.format(t+1, s))
            break


#============================================
# # 교수님 코드
# def isCheck(st):
#     #st이 회문이면 True
#     #아니면 False 를 return
#     st = 0
#     ed = len(s) - 1
#     while st < ed and s[st] == s[ed]:
#         st += 1
#         ed -= 1
#     if st >= ed:
#         return True
        
#     return False

# def CC():
#     #회문을 찾아서 return
#     #가로
#     # for row in range(N):
#     #     for st in range(N-M+1):
#     #         result = isCheck(ARR[row][st:str+M])
#     #         if result:
#     #             retrun ARR[row][st:st + M]

#     # #세로
#     # for col in range(N):
#     #     for st in range(N-M+1):
#     #         temp_str = ""
#     #         for k in range(st, st+M):
#     #             temp_str += ARR[k][col]
#     #         result = isCheck(temp_str)
#     #         if result:
#     #             return temp_str


#     for i in range(N):
#         for st in range(N-M+1):
#             #가로
#             result = isCheck(ARR[i][st:st+M])
#             if result:
#                 return ARR[i][st:st+M]
#             #세로
#             temp_str = ""
#             for k in range(st, st+M):
#                 temp_str += ARR[k][i]
#             result = isCheck(temp_str)
#             if result:
#                 return temp_str



# import sys
# sys.stdin = open('4861_input.txt', 'r')

# tc = int(input())

# for t in range(tc):
#     N, M = map(int, input().split())
#     ARR = [input() for _ in range(N)]



#가로축순회 하고 회문 못찾으면 세로축순회
#가로축 처음인덱스와 끝인덱스 비교비교비교

# T = int(input())
# for tc in range(1, T+1):
#     n, m = map(int,input().split())
#     arr = [input() for _ in range(n)]
#     result = 0
#     newnewarr=[]
#     # 가로축에서 회문 찾기
#     for i in range(n): # 0 1 2 3 4 5 6 7 8 9
#         for j in range(n-m+1): # 0 1 2 3 4
#             if arr[i][j:j+m] == arr[i][j:j+m][::-1]:
#                 result = ''.join(arr[i][j:j+m])

#     # 세로축에서 회문 찾기
#     # 세로축은 슬라이싱 안되니까 행 열 자리 바꿔주자
#     for i in range(n):
#         newarr = []
#         for j in range(n):
#             newarr += arr[j][i]
#         newnewarr.append(''.join(newarr))

#     for i in range(n): # 0 1 2 3 4 5 6 7 8 9
#         for j in range(n-m+1): # 0 1 2 3 4
#             if newnewarr[i][j:j+m] == newnewarr[i][j:j+m][::-1]:
#                 result = ''.join(newnewarr[i][j:j+m])

#     print(f'#{tc} {result}')

#============================================
tc = int(input())

for t in range(1, tc+1):
    squareLen, strLen = map(int, input().split())
    inputList = [input() for _ in range(squareLen)]
    strList = []
    result = ''

    #가로
    for l in inputList:
        for i in range(squareLen - strLen +1):
            strList.append(l[i: i+strLen])

    #세로
    for i in range(squareLen):
        for j in range(squareLen - strLen + 1):
            sumStr = ''
            for k in range(strLen):
                sumStr += inputList[k+j][i]
            strList.append(sumStr)
    
    for strV in strList:
        sameStr = ''
        for s in range(strLen//2):
            if strV[s] != strV[strLen -s -1]:
                break
            sameStr += strV[s]
        if strV[0: strLen//2] == sameStr:
            result = strV
            break
    
    print('#{} {}'.format(t, result))

#============================================
tc = int(input())

for t in range(1, tc+1):
    squareLen, strLen = map(int, input().split())
    strList = [input() for _ in range(squareLen)]
    restrictStrList = []

    for i in range(squareLen):
        verticalStr = ''
        for j in range(squareLen):
            verticalStr += strList[j][i]
        strList.append(verticalStr)
    
    for l in strList:
        for i in range(squareLen - strLen + 1):
            restrictStrList.append(l[i:i+strLen])
    
    for strV in restrictStrList:
        sameStr = ''
        for s in range(strLen//2):
            if strV[s] != strV[strLen -s -1]:
                break
            sameStr += strV[s]
        if strV[0: strLen//2] == sameStr:
            result = strV
            break
    
    print('#{} {}'.format(t, result))



