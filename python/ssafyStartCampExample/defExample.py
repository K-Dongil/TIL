import random
def get_lotto_number():
    numbers = range(1, 46)
    pick = random.sample(numbers, 6)
    return pick
# 다른 곳에서 쓰려고 할 때 
# import lotto
# lotto.get_lotto_number()