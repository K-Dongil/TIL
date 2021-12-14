tc = int(input())

for t in range(1, tc+1):
    max_day, today_percent, yesterday_percent = map(int, input().split())
    game_result = 'Broken'
    day = 0
    now_win = 0
    
    for i in range(1, max_day+1): # 전체 날자
        for j in range(1, i+1): # 이긴 날자
            if (j / i) * 100 == yesterday_percent:
                day = i
                now_win = j
                break

    if max_day < day:
        pass
    else:
        remain_day = max_day - day
        continue_win = now_win
        continue_lose = now_win
        
        for i in range(remain_day):
            day += 1
            continue_win += 1
            if (continue_win / day) * 100 == today_percent or (continue_lose / day) * 100 == today_percent:
                game_result = 'Possible'
                break
    
    print(game_result)
    
        
