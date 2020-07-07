def merge_sort(items):
    if len(items) > 1:
        mid = len(items) // 2
        left = items[:mid]
        right = items[mid:]

        merge_sort(left)
        merge_sort(right)

        merge(items, left, right)


def merge(items, left, right):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            items[k] = left[i]
            i += 1
        else:
            items[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        items[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        items[k] = right[j]
        j += 1
        k += 1
