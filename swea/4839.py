def binary_search(page, want_page):
    page_lst = list(range(page))
    start_page = 1
    # end_page = page
    cnt = 0
    while start_page <= page:
        open_page = (start_page + page)//2
        if open_page == want_page:
            return cnt
        elif open_page < want_page:
            start_page = open_page # 일반적인 binary_search를 생각하면 시작점 = 중간지점 +1해줘야겠지만 문제를 읽어보면 그냥 중간이였던 부분을 시작점으로 잡았다 
            cnt += 1
        elif open_page > want_page:
            page = open_page
            cnt += 1

def winner(a, b):
    result = ''
    if a > b:
        result ='B'
    elif a < b:
        result ='A'
    elif a == b:
        result = 0
    return result

t = int(input())

for i in range(t):
    page, a_want_page, b_want_page = map(int, input().split())
    a_result = binary_search(page, a_want_page)
    b_result = binary_search(page, b_want_page)

    result = winner(a_result, b_result)

    print('#{} {}'.format(i+1, result))


#==================================
def binary_search(allPage, findPage):
    leftPage = 1
    rightPage = allPage
    middlePage = allPage//2
    cnt = 1

    while leftPage <= rightPage:
        if middlePage < findPage:
            leftPage = middlePage
        elif middlePage > findPage:
            rightPage = middlePage
        else:
            return cnt

        middlePage = (leftPage + rightPage)//2
        cnt += 1

    return 0

tc= int(input())

for t in range(1, tc+1):
    allPage, aFindPage, bFindPage = map(int, input().split())
    win = 0

    aFind = binary_search(allPage, aFindPage)
    bFind = binary_search(allPage, bFindPage)

    if aFind < bFind:
        win = 'A'
    elif aFind > bFind:
        win = 'B'

    print('#{} {}'.format(t, win))