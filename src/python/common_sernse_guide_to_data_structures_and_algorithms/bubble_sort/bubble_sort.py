def bubble_sort(items):
    ordered = False

    while not ordered:
        ordered = True
        for i in range(len(items)):
            j = i + 1
            if j <= (len(items) - 1) and items[i] > items[j]:
                items[i], items[j] = items[j], items[i]
                ordered = False


def recursive_bubble_sort(items, size):
    if size <= 1:
        return

    for i in range(size):
        j = i + 1
        if j < size and items[i] > items[j]:
            items[i], items[j] = items[j], items[i]

    return recursive_bubble_sort(items, size - 1)
