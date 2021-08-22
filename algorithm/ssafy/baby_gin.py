# 0 ~ 9까지의 숫자 중 6개의 카드를 뽑았을 때 3장의 카드가 연속적인 번호일 때 run, 3장의 카드가 동일한 번호를 갖는 경우 triplet
lst =[4, 4, 4, 3, 4, 5] # 6장의 카드가 이렇게 뽑혔다고 했을 때
counts = [0] * 10 # 0 ~ 9
run_i =0 # run을 조사할 때 index대신 쓰일 변수
triplet_i = 0 # triplet을 조사할 때 index대신 쓰일 변수
run = 0 # 6장의 카드 중 run인 경우 수
triplet = 0 # 6장의 카드 중 triplet인 경우 수

# counts 배열 만든다
for i in lst: # 리스트에 담겨진 값들을 i에 담아 반복
    counts[i] += 1 # counts 배열의 i번째의 값에 1을 더한다

# run 조사
while run_i <= len(counts)-3: # 6장의 카드 중 3개의 번호가 연속적인지 비교할 것, counts배열에서 len(counts)-3까지의 index까지 고려
    if 1 <= counts[run_i] and 1 <= counts[run_i + 1] and 1 <= counts[run_i + 2]: # 연속된 3개의 번호가 있다면
        run += 1 # run 개수가 1증가
        counts[run_i] -= 1 # 3장으로 1개의 run을 구성했으므로 counts배열에서 1씩 뺀다
        counts[run_i + 1] -= 1
        counts[run_i + 2] -= 1
        continue # 그리고 index번호가 늘어나지 않고 다시 제자리에서 시작하여 또 연속된지 확인
    run_i += 1 # 연속된 번호가 없다면 index 증가

# triplet조사
while triplet_i < len(counts): # counts배열을 모두 조사할 것 이므로
    if 3 <= counts[triplet_i]: # 3개의 같은 번호가 있다면
        triplet += 1 # triplet 개수 증가
        counts[triplet_i] -= 3 # 3장으로 1개의 triplet을 구성했으므로 counts배열에서 3을 뺀다
    triplet_i += 1 # 3개의 같은 번호가 없다면 index 증가

if 2 <= run or (1 <= run and 1<= triplet) or 2 <= triplet: # run + run, run+triplet, triplet + triplet인지 조사
    print('baby-gin')
else:
    print('not baby-gin')