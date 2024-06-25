numbers = [20, 22, 56, 48, 18, 29, 3, 30]

lowest_number = numbers[0]
for number in numbers:
    if number < lowest_number:
        lowest_number = number
print(lowest_number)
