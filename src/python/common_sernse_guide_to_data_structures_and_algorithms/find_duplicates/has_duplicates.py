def has_duplicates(items):
    for i in range(len(items)):
        for j in range(len(items)):
            if i != j and items[i] == items[j]:
                return True
    return False


def has_duplicates_with_buffer(items):
    duplicates = []
    for item in items:
        if item not in duplicates:
            duplicates.append(item)
        else:
            return True
    return False
