import json


def menu_count(restorant):
    pass
    # 여기에 코드를 작성합니다.
    

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    restorant_json = open('problem02_data.json', encoding='UTF8')
    restorant = json.load(restorant_json)
    print(menu_count(restorant)) 
    # => 4