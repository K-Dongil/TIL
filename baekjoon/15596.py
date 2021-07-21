def solve(a): # 함수명 solve, 매개변수를 한개 받는다
    ans = 0 # 리스트에 있는 정수 n개 합친 값을 담아 줄 변수
    for i in range(len(a)): # 리스트 길이만큼 for문 반복
        ans += a[i] # 리스트 i번째 있는 정수를 ans 변수에 합쳐준다
    return ans # 합친 값 return