a_list = []

for i in range(10):
    a_list.append(int(input()))

a_list = list(map(a, a_list))
print(a_list)
def a(item):
    return item%42