"""
What is an Inversion?
An inversion occurs when two elements in the array are out of order. Specifically, if there are two elements A[i] and A[j] such that:

i < j (they appear in this order in the array), but
A[i] > A[j] (the value at A[i] is greater than the value at A[j]).
Example:

Array: [3, 1, 2]

Inversion: 3 > 1 (index 0 and 1)
Inversion: 3 > 2 (index 0 and 2)
Total inversions = 2.
"""

from typing import List


def count_number_of_inversion(arr: List[int]) -> int:
    counter = 0
    for i, value in enumerate(arr):
        for j in range(i + 1, len(arr)):
            if value > arr[j]:
                counter += 1

    return counter


arr = [3, 1, 2]
inversions = count_number_of_inversion(arr)
print(f"Number of inversion: {inversions}")
