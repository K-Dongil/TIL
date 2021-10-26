def permutations(lst, num):
    if num==0:
        return [[]]
    cases = []
    for i in range(len(lst)):
        for case in permutations(lst, num-1):
            print(case)
            cases.append( [lst[i]]+case )
            print(cases)
    return cases

print(permutations([1,2,3], 2))