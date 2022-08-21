arr = [ [1,2,3],
        [4,5,6],
        [9,8,9]]

# Solution 1
val = 0
val2 = len(arr)-1

left_to_right = 0
right_to_left = 0

# for i in arr:
#     left_to_right += i[val]
#     val += 1
#     right_to_left += i[val2]
#     val2 -= 1

# print(abs(left_to_right - right_to_left))

# Solution 2
for count, item in enumerate(arr):
    left_to_right += item[count]
    right_to_left += item[(len(arr)-1)-count]

print(abs(left_to_right - right_to_left))
