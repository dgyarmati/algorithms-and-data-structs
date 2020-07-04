def insertion_sort(items):
    for i in range(1, len(items)):
        position = i
        temp_item = items[i]

        while position > 0 and items[position - 1] > temp_item:
            items[position] = items[position - 1]
            position -= 1

        items[position] = temp_item
