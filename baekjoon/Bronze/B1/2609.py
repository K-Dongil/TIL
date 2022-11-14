num1, num2 = map(int, input().split())
rangeV = num2//2 if num1 < num2 else num1//2
gcd = 0
lcm = num2

# 최대 공약수
for i in range(rangeV, 2, -1):
    if num1 % i == 0 and num2 % i == 0:
        gcd = i
        break

# 최소 공배
while True:
    lcm = 2*lcm
    if lcm % num1 == 0:
        break



print(gcd)
print(lcm)