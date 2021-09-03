from django.shortcuts import render
import requests
import random

def bubbleSort(lst):
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]

# Create your views here.
def lotto(request):
    result = []
    cnt = 0
    my_lotto = random.sample(range(1 ,46), 6)
    bubbleSort(my_lotto)
    for i in range(1, 501):
        url = f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={i}'
        response = requests.get(url)
        lotto = response.json()
        bonus_num = lotto['bnusNo']
        winno = []
        for i in range(1,7):
            winno.append(lotto[f'drwtNo{i}'])
        for i in range(6):
            if my_lotto[i] == winno[i]:
                cnt += 1
        if cnt == 6:
            result.append(1)
        elif (bonus_num in my_lotto) and cnt == 5:
            result.append(2)
        elif cnt == 5:
            result.append(3)
        elif cnt == 4:
            result.append(4)
        elif cnt == 3:
            result.append(5)

    context = {
        'one':result.count(1),
        'two':result.count(2),
        'three':result.count(3),
        'four':result.count(4),
        'five':result.count(5),
        'my_lotto':my_lotto,
        'result':result
    }
    return render(request, 'pages/lotto.html', context)