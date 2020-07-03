def bubble_sort(items):
    ordered = False

    while not ordered:
        ordered = True
        for i in range(len(items)):
            j = i + 1
            if j <= (len(items) - 1) and items[i] > items[j]:
                items[i], items[j] = items[j], items[i]
                ordered = False
