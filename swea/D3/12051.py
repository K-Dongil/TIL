tc = int(input())
result_lst = [0] * tc

for t in range(1, tc+1):
    today, today_percent, total_percent = map(int, input().split())
    game_result = 'Possible'

    if today == 1 and not (today_percent in [0, 100]):
        game_result ='Broken'
    elif 2 <= today <= 3 and not (today_percent in [0, 50, 100]):
        game_result ='Broken'
    elif today == 4 and not (today_percent in [0, 25 ,50, 100]):
        game_result ='Broken'
    elif 5 <= today <= 9 and not (today_percent in [0, 20 , 25 ,50, 100]):
        game_result ='Broken'
    elif 10 <= today <= 19 and not (today_percent in [0, 10, 20 , 25 ,50, 100]):
        game_result ='Broken'
    elif 20 <= today <= 49 and not (today_percent in [0, 5, 10, 20 , 25 ,50, 100]):
        game_result ='Broken'
    elif 50 <= today <= 99 and not (today_percent in [0, 2, 5, 10, 20 , 25 ,50, 100]):
        game_result ='Broken'

    if (total_percent == 0 and today_percent != 0) or (total_percent == 100 and today_percent != 100):
        game_result = 'Broken'

    result_lst[t-1] =  f'#{t} ' + game_result

for result in result_lst:
    print(result)