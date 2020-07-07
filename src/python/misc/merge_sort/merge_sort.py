"""
Description:
1. divide array to smaller arrays (left, right) until there's only one element in the divided arrays (which means that they are sorted)
2. merge the small arrays while sorting them:
    - while left and right have elements:
        - add smaller element to temporary array
        - remove the previously added element from the respective array (left or right)
    - now that left or right is empty:
        - take the array (left or right) which still has elements, add their items to temp array
        - remove the added element from respective array

    properties:
        O(N log N)
        stable
        external - can sort things which do not fit in main memory, can handle massive amounts of data
        out of place
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
