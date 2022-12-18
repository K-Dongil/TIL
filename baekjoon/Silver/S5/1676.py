factorialNum = int(input())
factorialList = [1] * (factorialNum+1)
result = 0

for i in range(2, factorialNum+1):
    factorialList[i] = i * factorialList[i-1]


for s in str(factorialList[factorialNum])[::-1]:
    if s == '0':
        result += 1
    else:
        break

print(result)