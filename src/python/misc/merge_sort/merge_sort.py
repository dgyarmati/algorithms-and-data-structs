"""
Description:
1. divide array to smaller arrays until there's only one element in the divided arrays (which means that they are sorted)
2. merge the small arrays while sorting them:
    - loop through the split arrays, and add the smaller items to the original array, overwriting items in the original array
    - add the rest of the items to the array from the split arrays

    watch out for advancing all index pointers - left, right and that of the original array!
"""


def merge_sort(items):
    if len(items) > 1:
        mid = len(items) // 2
        left = items[:mid]
        right = items[mid:]

        merge_sort(left)
        merge_sort(right)

        merge(items, left, right)


def merge(array, left, right):
    left_idx = right_idx = array_idx = 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            array[array_idx] = left[left_idx]
            left_idx += 1
        else:
            array[array_idx] = right[right_idx]
            right_idx += 1
        array_idx += 1

    while left_idx < len(left):
        array[array_idx] = left[left_idx]
        left_idx += 1
        array_idx += 1

    while right_idx < len(right):
        array[array_idx] = right[right_idx]
        right_idx += 1
        array_idx += 1
