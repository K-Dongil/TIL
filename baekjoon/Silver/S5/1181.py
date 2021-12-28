def lenSort():
    for i in range(unit):
        for j in range(i, unit):
            if len(words[i]) > len(words[j]):
                words[i], words[j] = words[j], words[i]

def alphaSort():
    memory = 0
    for i in range(unit):
        for j in range(i, unit):
            
            momory = words[i] 
            if words[i] > words[j]:
                words[i], words[j] = words[j], words[i]

unit = int(input())
words = [''] * unit
for i in range(unit):
    words[i] = input()

solve()
# words.sort()
print(words)
