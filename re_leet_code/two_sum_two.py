# as the list sorted then we can use two pointer
# left pointer: we will move left pointer if sum of two pointer is less then target
# right pointer: we will move right pointer if sum of two pointer is greater then target

class Solution(object):
    def twoSum(self, numbers, target):
        # let declear two pointer
        # left pointer will start from begiaing of th list
        left_pointer = 0
        # right pointer will start from endpoint the list
        right_pointer = len(numbers) - 1
        # we need to check for sum of two pointer pointer untill left and right pointer value dosen't match
        while left_pointer < right_pointer:
            # first check if sum is the target
            sum_value = numbers[left_pointer] + numbers[right_pointer]
            if sum_value == target:
                # if we found the target then we need to return the index
                # but as index starts from 1 not 0 so we are adding 1
                return [left_pointer+1, right_pointer+1]
            # if sum_value is not the target value then we need to adjust the pointer
            # if sum_value is less then target then move the left pointer
            if sum_value < target:
                left_pointer += 1
            else:
                right_pointer -= 1
        
        

numbers =  [2,3,4]
target = 6
solution = Solution().twoSum(numbers, target)
solution
