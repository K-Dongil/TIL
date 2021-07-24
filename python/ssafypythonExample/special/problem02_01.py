# 판매하는 메뉴의 개수 반환
import json

# def menu_count(restorant):
#     return len(restorant['menus'])

def menu_count(restorant):
    num = 0
    for i in restorant['menus']:
        num += 1
    return num
    

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    restorant_json = open('problem02_data.json', encoding='UTF8')
    restorant = json.load(restorant_json)
    print(menu_count(restorant)) 
    # => 4