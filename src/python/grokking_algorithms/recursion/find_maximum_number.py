def find_maximum_number(numbers):
    if len(numbers) == 2:
        return numbers[0] if numbers[0] > numbers[1] else numbers[1]
    sub_max = find_maximum_number(numbers[1:])
    return numbers[0] if numbers[0] > sub_max else sub_max
