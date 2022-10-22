T = int(input())

for i in range(T):
    max_energy, station_num, recharge_num = map(int, input().split())
    recharge_station_list = list(map(int, input().split()))
    now_station = 0
    now_energy = max_energy
    recharge = 0
    idx = 0

    while True:
        now_station += 1
        now_energy -= 1

        if idx < len(recharge_station_list)-1:
            if now_energy < (recharge_station_list[idx + 1] - now_station) and (now_station in recharge_station_list):
                recharge += 1
                now_energy = max_energy

        if idx == len(recharge_station_list)-1:
            if now_energy < (station_num - now_station) and (now_station in recharge_station_list):
                recharge += 1
                now_energy = max_energy

        if now_station == station_num:
            break

        if now_energy ==0 and (now_station not in recharge_station_list):
            recharge = 0
            break

        if now_station in recharge_station_list:
            idx += 1

    print('#{} {}'.format(i+1, recharge))


# ====================================================
# 이 코드는 충전소 위치랑 충전해야하는 시점이 딱 맞아 떨어질 때만 충전하도록 구현
# T = int(input())
#
# for i in range(T):
#     max_energy ,station_num, recharge_num = map(int, input().split())
#     recharge_station_list = list(map(int, input().split()))
#     now_station = 0
#     now_energy = max_energy
#     recharge = 0
#
#     while True:
#         now_station += 1
#         now_energy -= 1
#         print(now_station)
#         print(now_energy)
#         if now_energy == 0 and (now_station in recharge_station_list):
#             recharge += 1
#             now_energy = max_energy
#
#         elif now_station == station_num:
#             break
#
#         elif now_energy ==0 and (now_station not in recharge_station_list):
#             recharge = 0
#             break
#
#     print('#{} {}'.format(i+1, recharge))


#===================================================================
tc = int(input())

for t in range(tc):
    goEnergy, end, rechargeStation = map(int, input().split())
    rechargeStations = list(map(int, input().split()))
    rechargeStations.append(end)
    
    nowEnergy = goEnergy
    nowStation = 0
    rechargeNumber = 0
    

    for i in range(0, end):
        if i != 0:
            nowEnergy -=1
        if i in rechargeStations:
            print(i)
            if nowEnergy < rechargeStations[1]-i:
                rechargeNumber += 1
                nowEnergy = goEnergy
            rechargeStations.pop(0)
        if nowEnergy == 0:
            rechargeNumber = 0
            break
            
    print('#{} {}'.format(t+1, rechargeNumber))
