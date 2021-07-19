H, M = map(int, input().split())
H = H * 60 + M -45
if H < 0:
    H = 24*60 + M - 45
print(H // 60, H % 60)