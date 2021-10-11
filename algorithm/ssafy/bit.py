x = 0x01020304
p = []
for i in range(0, 4):
    p.append((x >> (i*8)) & 0xff)

print("x = %d%d%d%d" % (p[0], p[1], p[2], p[3]))
