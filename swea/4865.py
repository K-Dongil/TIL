def max_num(dic):
    best_count = 0
    for i in dic:
        if best_count < dic[i]:
            best_count = dic[i]
    return best_count

def count_element(dic, str):
    for key in dic:
        for s in str:
            if key == s:
                dic[key] += 1
    return  dic

tc = int(input())

for t in range(tc):
    str1 = input()
    str2 = input()

    char_dict = {}

    for s in str1:
        char_dict[s] = 0

    count_dic = count_element(char_dict, str2)
    
    
    print('#{} {}'.format(t+1, max_num(count_dic)))


# # 교수님 코드
# TC =int(input())

# for tc in range(1, TC+1):
#     str1 = input()
#     str2 = input()

#     myDict = {}
#     for c in str1:
#         if c not in myDict:
#             myDict[c] = 0
    
#     for c in str2:
#         if c in myDict:
#             myDict[c] += 1
    
#     maxV = 0
#     for i in myDict.values():
#         if i > maxV:
#             maxV = i
    
#     print('#{} {}'.format(tc, maxV))