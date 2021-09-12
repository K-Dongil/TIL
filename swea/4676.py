def combine(lst):
    str = ''
    for l in lst:
        str += l
    return str

tc = int(input())

for t in range(tc):
    str = list(input())
    hypen = int(input())
    position = list(map(int, input().split()))
    result = ''
    for i in position:
        posi = 0
        gogo = 0
        for s in str:
            posi += 1 
            if s != '-':
                gogo += 1
                if i == 0 and gogo -1 == 0:
                    str.insert(posi-1, '-')
                    break
                if gogo == i:
                    str.insert(posi, '-')
                    break
    
    result = combine(str)
    print(f'#{t+1} {result}')