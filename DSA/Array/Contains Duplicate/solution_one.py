def solution(nums):
    """takes an array and checks if it contains duplicate"""

    # converting list into set and storing them in `nums_set`
    nums_set = set(nums)
    # returning the compared result
    return len(nums) != len(nums_set)


array_one = [1, 2, 3, 1]  # example: 1
array_two = [1, 2, 3, 4]  # example: 2
array_three = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]  # example: 3


result_one = solution(array_one)
print(result_one)  # False

result_two = solution(array_two)
print(result_two)  # True

result_three = solution(array_three)
print(result_three)  # False
