def find_intersection(array_1, array_2):
    intersection = []

    for item_1 in array_1:
        for item_2 in array_2:
            if item_1 == item_2:
                intersection.append(item_1)
                break

    return intersection
