tc = int(input())

for t in range(1, tc+1):
    N =int(input())
    result = "No"

    for i in range(1, 10):
        if (N//i) * i == N and 1 <= N/i <= 9:
            result = "Yes"
            break

    print(f'#{t} {result}')

# tc = int(input())

# for t in range(1, tc+1):
#     N =int(input())
#     result = "No"

#     for i in range(1, 10):
#         for j in range(1, 10):
#             if i*j == N:
#                 result = "Yes"
#                 break
    
#     print(f'#{t} {result}')