i = 15 #0b01111

for j in range(4, -1, -1):
	r = i & (1<<j)
	if r:
		print('1', end='')
	else:
		print('0', end='')
# 출력 결과 01111


# i = 14 #0b01110
#
# for j in range(5):
# 	r = i & (1<<j)
# 	if r:
# 		print('1', end='')
# 	else:
# 		print('0', end='')
# # 출력 결과 01110