strList = []
strInput = (input()).upper()
strSet = set(strInput)
for i in strSet:
    strList.append((i, strInput.count(i)))
print(strList)