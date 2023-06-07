
def majorityElement(nums):
    hash_table = {}
    for digit in nums:
        if hash_table.get(digit, None):
            
            hash_table[digit] += 1
        else:
            hash_table[digit] = 1
    print(max(hash_table, key=hash_table.get))

    
nums = [3,2,3,2,2,4]
majorityElement(nums)