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
