
import doctest
from typing import List


def merge_sort(arr: List[int]) -> List[int]:
    """ Implementation of merge sort

    >>> merge_sort([5, 3, 3])
    [3, 3, 5]

    >>> merge_sort([5, -2, -44, 8, 44, 3, 3])
    [-44, -2, 3, 3, 5, 8, 44]

    >>> merge_sort([5, 3, -3])
    [-3, 3, 5, 6]

    >>> merge_sort([])
    []

    >>> merge_sort([0])
    [0]

    """
    if len(arr) > 1:
        left = arr[:len(arr) // 2]
        right = arr[len(arr) // 2:]
        left_sorted = merge_sort(left)
        right_sorted = merge_sort(right)
        sorted = []

        left_index = 0
        right_index = 0

        while left_index < len(left_sorted) and right_index < len(right_sorted):
            if left_sorted[left_index] <= right_sorted[right_index]:
                sorted.append(left_sorted[left_index])
                left_index += 1
            else:
                sorted.append(right_sorted[right_index])
                right_index += 1
        
        while left_index < len(left_sorted):
            sorted.append(left_sorted[left_index])
            left_index += 1
        
        while right_index < len(right_sorted):
            sorted.append(right_sorted[right_index])
            right_index += 1
        
        arr = sorted

    return arr

doctest.testmod()

