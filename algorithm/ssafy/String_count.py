cnt = [0] * 26 # 배열은 a ~ z가 몇번 들어있는지 저장되어 있다.
s ='aba'
for x in s:
	cnt[ord(x) - ord('a')] += 1 # 가장 낮은 값인 a의 ascii코드 값을 빼주면 배열에서의 문자위치를 알아낼 수 있다
print(cnt)

cnt1 = [0] * 52 # 배열은 a ~ Z가 몇번 들어있는지 저장되어 있다.
s1 ='aB1a'
for x in s1:
    if 'a' <= x <= 'z':
        cnt1[ord(x)-ord('a')] += 1 # 가장 낮은 값인 a의 ascii코드 값을 빼주면 배열에서의 문자위치를 알아낼 수 있다. (소문자에 한해서만)
    elif 'A' <= x <= 'Z':
        cnt1[ord(x) - ord('A') + 26] += 1
    elif '0' <= x <= '9':
        print('숫자')
print(cnt1)


cnt2 = [0] * 61 # 배열은 0~9, a ~ Z가 몇번 들어있는지 저장되어 있다.
s2 ='aB1a'
for x in s2:
    if 'a' <= x <= 'z':
        cnt2[ord(x)-ord('a')] += 1 # 가장 낮은 값인 a의 ascii코드 값을 빼주면 배열에서의 문자위치를 알아낼 수 있다. (소문자에 한해서만)
    elif 'A' <= x <= 'Z':
        cnt2[ord(x) - ord('A') + 26] += 1
    elif '0' <= x <= '9':
        cnt2[51 + int(x)] += 1
print(cnt2)