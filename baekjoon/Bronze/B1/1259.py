input_data = input()
len_data = len(input_data)
result = "yes"

for i in range(len_data//2):
    if input_data[i] == input_data[len_data-1- i]:
        pass
    else:
        result = "no"
        break

print(result)