# https://www.hackerrank.com/challenges/larrys-array/problem

from typing import List


def count_number_of_inversion(arr: List[int]) -> int:
    counter = 0
    for i, value in enumerate(arr):
        for j in range(i + 1, len(arr)):
            if value > arr[j]:
                counter += 1

    return counter


def larrys_array_self(A):
    # Write your code here
    counter = count_number_of_inversion(A)
    if counter % 2 == 0:
        return "YES"
    else:
        return "NO"


def larrysArray(A):
    n = len(A)

    # Try to sort using the rotation operation
    for i in range(n - 2):
        # While the segment [i, i+1, i+2] is unsorted, perform rotations
        while A[i] > A[i + 1] or A[i] > A[i + 2]:
            # Perform a rotation [A[i], A[i+1], A[i+2]] -> [A[i+1], A[i+2], A[i]]
            A[i], A[i + 1], A[i + 2] = A[i + 1], A[i + 2], A[i]
            # If the segment is sorted, break out
            if A[i] <= A[i + 1] <= A[i + 2]:
                break

    # Check if the array is sorted
    return "YES" if A == sorted(A) else "NO"
