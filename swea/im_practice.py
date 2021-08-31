# 버튼을 누를때마다 버튼의 배수에 위치한 led들이 켜지고 꺼진다 (버튼은 자리가 1부터 시작), 원하는 led구조를 만들기 위해 버튼을 최소한 몇 번 눌러야 하는가?
# 입력 테스트케이스, led개수, led구조
# 출력 : 원하는 led구조를 위해서 버튼 누르는 최소한의 횟수
# 뒤에서부터 바꾸면 앞에 영향을 주기 때문에 앞에서부터 차례대로 비교해나가야한다
tc = int(input())

for t in range(tc):
    led_button = int(input())
    want_led = list(map(int, input().split()))
    default_led = [0] * led_button
    idx = 1
    count = 0

    while True:
        if want_led == default_led:
            break
        if default_led[idx-1] != want_led[idx-1]:
            count += 1
            for i in range(idx, led_button+1):
                if not i % idx:
                    if default_led[i-1] == 1:
                        default_led[i-1] = 0
                    elif default_led[i-1] == 0:
                        default_led[i-1] = 1
        idx += 1
    print('#{} {}'.format(t+1, count))

"""
5
5 
1 1 0 0 1 
6 
0 1 1 1 0 0 
7 
1 1 1 1 1 1 1 
10 
0 1 0 1 0 1 0 1 0 1 
20 
0 0 0 0 1 0 0 1 0 1 0 1 0 1 0 1 1 1 0 0

출력 : 
3 2 1 1 8
"""