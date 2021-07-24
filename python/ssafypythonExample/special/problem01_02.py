# 60점 이상인 과목의 개수 계산
import json

def over(scores):
    num = 0
    for score in scores:
        if score >= 60:
            num +=1
    return num
    # 여기에 코드를 작성합니다.


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    scores_json = open('problem01_data.json', encoding='UTF8')
    scores = json.load(scores_json)
    print(over(scores)) 
    # => 3