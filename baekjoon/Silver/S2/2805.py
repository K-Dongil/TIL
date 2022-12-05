def binary(lst):
    start = 0
    end = max(lst)
    maxCutter = 0
    while start <= end:
        middle = (start + end)//2
        getTree = 0
        for tree in trees:
            getTree += tree - middle if 0 < tree - middle else 0
        if needTree <= getTree:
            start = middle + 1
            if maxCutter < middle:
                maxCutter = middle
        elif needTree > getTree:
            end = middle - 1
    return maxCutter

treeNum, needTree = map(int, input().split())
trees = list(map(int, input().split()))
print(binary(trees))
