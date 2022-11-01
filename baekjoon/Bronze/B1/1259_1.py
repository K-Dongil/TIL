while True:
    word = input()
    wordLen = len(word)
    result = 'yes'
    
    if word == '0':
        break

    for i in range(wordLen // 2):
        if word[i] != word[wordLen - 1 - i]:
            result = 'no'
            break

    print(result)