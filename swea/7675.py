tc = int(input())

for t in range(1, tc+1):
    sentence_num = int(input())
    input_lst = input().split()
    sentence_lst = [[] for _ in range(sentence_num)]
    idx = 0
    name_lst = []

    for lst in input_lst:
        sentence_lst[idx].append(lst)
        if '!' in lst or '?' in lst or '.' in lst:
            idx += 1

    for sentence in sentence_lst:
        name = 0
        for word in sentence:
            if len(word) == 1 and word.isupper():
                name += 1
            elif not word[0:-1].isalpha():
                continue
            elif word[0].isupper() and word[-1].islower():
                name += 1
            elif word[-1] in ('!', '?', '.') and word[0].isupper() and word[-2].islower():
                name += 1

        name_lst.append(str(name))

    result = ' '.join(name_lst)
    print(f'#{t} {result}')