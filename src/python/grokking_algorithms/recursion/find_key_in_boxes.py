# def find_box_with_key(box):
#     for i in range(len(box)):
#         if not len(box[i]):
#             offset = i + 1
#             find_box_with_key(box[offset:])
#         else:
#             return box[i]


def find_box_with_key(box, i=0):
    if i == len(box):
        return None
    if "key" in box[i]:
        return box[i]
    else:
        i += 1
        return find_box_with_key(box, i)