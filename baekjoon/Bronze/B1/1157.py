word = input().upper()
alphabets = {w:0 for w in word}
cnt = 0
result = ''

for w in word:
    alphabets[w] += 1

for alphabet in alphabets:
    if cnt < alphabets[alphabet]:
        cnt = alphabets[alphabet]
        result = alphabet
    elif cnt == alphabets[alphabet]:
        result = '?'

print(result)