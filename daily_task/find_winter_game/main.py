# we will use while loop to iter over the arr until we have a winner
# take flag with value 0 and we will reset the value whenever we are working
# with new element of arr
# we will take min value from arr[0:1] then remove the value and append it to the list
# but it will required to take and store the max value in the current_max and update the flag value with 1
# next step if current value is new max then we update the flag with value thus flag is 2 so we have winner

import time


def getWinner(arr, k):
    limit = len(arr)
    counter = 0

    flag = 1
    current_max = None
    max_value = 0
    min_value = 0
    while True:
        if counter == limit:
            counter = 0

        if arr[0] > arr[1]:
            max_value = arr[0]
            min_value = arr[1]
        else:
            max_value = arr[1]
            min_value = arr[0]

        if current_max and current_max == max_value:
            flag += 1
        if current_max and current_max != max_value:
            flag = 1
        print(arr)
        print("=================================", max_value, flag)
        # print(arr)
        if flag == k:
            return max_value
        arr.remove(min_value)
        arr.append(min_value)
        current_max = max_value

        counter += 1


arr = [
    31,
    683,
    544,
    163,
    384,
    470,
    580,
    66,
    84,
    249,
    9,
    659,
    555,
    107,
    699,
    927,
    549,
    346,
    820,
    126,
    219,
    121,
    653,
    513,
    201,
    641,
    865,
    970,
    838,
    684,
    822,
    14,
    196,
    994,
    692,
    329,
    150,
    398,
    43,
    615,
    321,
    120,
    184,
    190,
    742,
    810,
    427,
    535,
    971,
    448,
    180,
    933,
    756,
    955,
    969,
    495,
    383,
    401,
    666,
]
# arr = [1, 11, 22, 33, 44, 55, 66, 77, 88, 99]
# arr = [2, 1, 3, 5, 4, 6, 7]
# arr = [3,2,1]
k = 14

print(getWinner(arr=arr, k=k))
