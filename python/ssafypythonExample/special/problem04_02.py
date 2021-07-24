# 유저 아이디의 마지막 글자가 0~9라면 True 아니라면 False반환
def is_id_valid(user_data):
    userId = user_data['id']
    result = ''
    for i in range(10):
        if userId[len(userId)-1] == str(i):
            result = True
            break
    else:
        result = False
    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    user_data1 = {
        'id': 'jungssafy5',
        'password': '1q2w3e4r',
    }
    print(is_id_valid(user_data1)) 
    # True
    
    user_data2 = {
        'id': 'kimssafy!',
        'password': '1q2w3e4r',
    }
    print(is_id_valid(user_data2)) 
    # False