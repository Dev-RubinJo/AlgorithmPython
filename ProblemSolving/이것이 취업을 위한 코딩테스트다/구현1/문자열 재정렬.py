str = input()

count = 0
array = []
for i in range(len(str)):
    if str[i].isdigit():
        count += int(str[i])
    else:
        array.append(str[i])
array.sort()
for i in array:
    print(i, end='')

print(count)