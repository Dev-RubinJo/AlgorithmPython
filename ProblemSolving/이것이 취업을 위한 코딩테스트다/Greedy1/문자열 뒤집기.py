numbers = input()

number_zero = 0
number_one = 0

for i in range(1, len(numbers)):
    if numbers[i - 1] != numbers[i]:
        if numbers[i] == '1':
            number_one += 1
        else:
            number_zero += 1
print(min(number_zero, number_one))
