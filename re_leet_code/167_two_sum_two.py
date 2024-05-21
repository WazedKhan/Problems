def twoSum(numbers, target):
    left_pointer = 0
    right_pointer = len(numbers) - 1
    while left_pointer < right_pointer:

        value = numbers[left_pointer] + numbers[right_pointer]
        if value > target:
            right_pointer -= 1
        elif value < target:
            left_pointer += 1
        else:
            value == target
            return [left_pointer + 1, right_pointer + 1]
    return
