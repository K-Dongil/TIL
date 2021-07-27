group_word_num = int(input())
word_list = []
group_word = 0
for i in range(group_word_num):
    word_list.append(input())
for word in word_list:
    group_word_list = [word[0]]
    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            group_word_list.append(word[i+1])
    for i in group_word_list:
        if group_word_list.count(i) != 1:
            break
        if i == group_word_list[len(group_word_list)-1]:
            group_word +=1
print(group_word)

#=====================================================
# group_word_num = int(input())
# word_list = []
# group_word = 0
# for i in range(group_word_num):
#     word_list.append(input())
# for word in word_list:
#     group_word_list = [word[0]]
#     for i in range(len(word)-1):
#         if word[i] != word[i+1]:
#             group_word_list.append(word[i+1])
#     group_word_list.sort()
#     print(len(group_word_list))
#     for i in range(len(group_word_list)):
#         if group_word_list[i] == group_word_list[i+1]:
#             break
#         if i == len(group_word_list)-1:
#             group_word += 1
# print(group_word)

#======================================================
# a = int(input())
# b = []
# c = 0
# for i in range(a):
#     b.append(input())
# for d in b:
#     e = [d[0]]
#     for i in range(len(d)-1):
#         if d[i] != d[i+1]:
#             e.append(d[i+1])
#     e.sort()
#     for i in e:
#         if e.count(i) != 1:
#             break
#         if i == e[len(e)-1]:
#             c +=1
# print(c)

#========================================================
# num = int(input())
# str = list(range(num))
# for i in range(num):
#     str[i] = input()
# chk = list(range(26)) # 소문자 개수만큼 리스트 선언 97 ~ 122
# def isgroup(str):
#         result = 0
#         a = []
#         chk = []
#         count = 0
#         l = len(str)
#         for i in range(len(str)):
#             a.append(str[i])
#         for i in range(26):
#             chk.append(0)
#         for i in range(l):  # 각 리스트 원소들 개수 세서 list에 저장
#             index = ord(str[i]) - 97
#             chk[index] += 1
#         for i in range(26):
#             if chk[i] != 0:  # 각 알파벳 등장 여부 list -> chk에 저장 됐는지 여부
#                 count += 1
#         if count == l:  # 모든 알파벳이 한번씩만 등장하면 그룹함수임
#             return 1
#         else :
#             for i in range(l):
#                 index = ord(str[i])-97
#                 if i != 0 and str[i] == str[i-1]: # 두번째 칸부터 연속된 수로 처리된것은 검사 안하고 넘김
#                     continue
#                 else:
#                     for j in range(chk[index]):
#                         if str[i+j] == str[i]:
#                             if i == l-1 :
#                                 return 1
#                         else :
#                             return 0
#         return 1
# countsum = 0
# for i in range(num):
#     countsum += isgroup(str[i])
# print (countsum)