T = int(input()) # 테스트 케이스 수

for i in range(T): # 위에서 입력받은 수만큼 for문을 돌린다
    info_lst = list(map(int, input().split())) # 공백을 기준으로 입력을 받고 int형으로 변환되어 map타입인 data를 list로 형변환

    a_price = info_lst[0] * info_lst[4] # 리스트에 첫번째로 담겨있는 값은 A사의 1L당 가격 * 네번째로 담겨있는 값은 집에서 사용한 수도 사용량 
    b_price = 0 # 아래에서 b사의 수도세를 조건문을 이용해 변수에 담아 줄 때 조건문 밖에서도 쓰기 위해 밖에서 변수를 초기화 시켜줬음

    if info_lst[2] >= info_lst[4]: # 만약 집에서 사용한 수도량이 월간 사용량보다 작다면
        b_price = info_lst[1] # b사의 요금은 기본 요금
    else: # 만약 집에서 사용한 수도량이 월간 사용보다 크다면
        b_price = info_lst[1] + info_lst[3] * (info_lst[4] - info_lst[2]) # 기본요금 + (초과했을 때 1L당 요금) + (사용한 수도량 - 월간 사용량)

    if a_price <= b_price: # a사의 요금보다 b사의 요금이 더 클 때
        print(f'#{i+1} {a_price}') # 테스트케이스 번호와 a사의 가격 출력
    else: # b사의 요금보다 a사의 요금이 더 클 때
        print(f'#{i+1} {b_price}') # 테스트케이스 번호와 b사의 가격 출력

##========================================================================
# T = int(input())

# for i in range(T):
#     P, Q, R, S, W = map(int, input().split())

#     a_price = P * W
#     b_price = 0

#     if R >= W:
#         b_price = Q
#     else:
#         b_price = Q + S * (W - R)
        
#     if a_price <= b_price:
#         print(f'#{i+1} {a_price}')
#     else:
#         print(f'#{i+1} {b_price}')