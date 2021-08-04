N = int(input())
num_list = list(map(int, input().split()))
count = 0
remove_num_list = list(num_list)
for i in num_list:
    if (i % 2 ==0) or (i % 3 ==0) or (i % 5 ==0) or (i % 7 ==0):
        if not (i == 2 or i == 3 or i == 5 or i ==7):
            remove_num_list.remove(i)
if 1 in remove_num_list:
    remove_num_list.remove(1)
print(len(remove_num_list))
