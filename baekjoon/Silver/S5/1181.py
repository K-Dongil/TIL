strNum = int(input())
strList = list(set([input() for _ in range(strNum)]))
result = ''

strList.sort() # 사전순 문자열 정렬
strList.sort(key = len) # 길이순 문자열 정렬

for l in strList:
    result += l + '\n'

print(result)