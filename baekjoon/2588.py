A = int(input())
B = int(input())
for i in range(len(str(B))-1, -1, -1):
    print(A * int((str(B)[i])))
print(A * B)