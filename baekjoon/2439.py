N = int(input())
for i in range(1, N+1):
    print(' ' * (N - i) + '*' * i)

# N = int(input())
# for i in range(1, N+1):
#     print(' ' * (N - i), end='\0')
#     print('*' * i)