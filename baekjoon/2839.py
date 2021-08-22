weight = int(input()) # 설탕의 무게를 입력받는다
bag = 0 # 설탕을 담는데 필요한 봉지의 수

while weight != 0: # 만약 무게가 0이 아니라면 계속해서 반복
    if weight % 5 and 3 <= weight: # 현재 남아있는 무게가 5의배수가 아니면서 3 이상일 때
        weight -= 3 # 무게에서 3kg을 뺀다
        bag += 1 # 봉지 수를 하나 늘린다
    elif weight % 5 == 0: # 만약 현재 무게가 5kg 봉지로 전부 담을 수 있다면
        bag += weight // 5 # 무게에서 5로 나눈 몫을 봉지 수에 더한다
        weight = weight % 5 # 그리고 무게는 0이 된다
    else: # 만약 3kg과 5kg봉지로 깔끔하게 못 담아낸다면
        bag = -1 # 실패출력을 위해 -1을 저장
        break # 그리고 반복문을 빠져나간다

print(bag) # 봉지 수 출력