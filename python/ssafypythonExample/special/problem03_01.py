# json에 저장된 데이터의 온도들을 리스트형태인 최고온도와, 최저온도로 나누고 dictionary형태로 출력
import json


def turn(temperatures):
    maxumumList = []
    minimumList = []
    for i in range(len(temperatures)):
        maxumumList.append(temperatures[i][0])
        minimumList.append(temperatures[i][1])
    maxMinDic = {
        'maximum':maxumumList,
        'minimum':minimumList
    }
    return maxMinDic
    # 여기에 코드를 작성합니다.


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    temperatures_json = open('problem03_data.json', encoding='UTF8')
    temperatures = json.load(temperatures_json)
    print(turn(temperatures)) 
    # =>
    # {
    #     'maximum': [9, 9, 11, 11, 8, 7, -4], 
    #     'minimum': [3, 0, -3, 1, -3, -3, -12]
    # }