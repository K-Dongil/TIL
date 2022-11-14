def euclidean(a, b):
    r = a % b
    if r == 0:
        return b
    return euclidean(b, r)

num1, num2 = map(int, input().split())
gcd = euclidean(num1, num2)
lcm = (num1 * num2 // gcd)

print(gcd)
print(lcm)