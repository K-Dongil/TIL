p = 'is' # 찾을 패턴
t = 'This is a book~!' # 전체 텍스트
M = len(p) # 찾을 패턴의 길이
N = len(t) # 전체 텍스트의 길이

def BruteForce(p,t):
    i = 0 # t의 인덱스
    j = 0 # p의 인덱스
    while j < M and i < N: # 주어진 영역을 벗어나지 않게 해줌, 패턴의 index 패턴을 벗어나지 않아야하고, 텍스트index가 text를 벗어나면 안된다?
        if t[i] != p[j]:
            i = i - j # 비교를 시작할 위치
            j = -1 # 초기화
        i = i + 1
        j = j + 1
    if j == M :
        return i - M # 검색 성공, 몇번째 index부터 찾고자하는 단어가 시작되는지
    else:
        return -1 # 검색 실패