def find_box_with_key(box):
    for i in range(len(box)):
        if not len(box[i]):
            offset = i + 1
            find_box_with_key(box[offset:])
        else:
            return box[i]

