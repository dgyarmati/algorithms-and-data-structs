def format_to_7_bit_binary_string(message_string):
    binary_values = []
    for char in message_string:
        binary_values.append('{0:07b}'.format(ord(char)))
    return "".join(binary_values)


def create_binary_list_with_separators(binary_string):
    current_char = binary_string[0]
    binary_with_separators_list = []
    for char in binary_string:
        if char != current_char:
            binary_with_separators_list.extend([":", char])
            current_char = char
        else:
            binary_with_separators_list.append(char)
    return binary_with_separators_list


def create_unary_string(binary_with_separators_list):
    unary_string = ""
    first_of_batch = True
    for char in binary_with_separators_list:
        if char == "1":
            chars = "0 0" if first_of_batch else "0"
            unary_string += chars
            first_of_batch = False
        elif char == "0":
            chars = "00 0" if first_of_batch else "0"
            unary_string += chars
            first_of_batch = False
        elif char == ":":
            unary_string += " "
            first_of_batch = True
    return unary_string


message = input()
binary_string = format_to_7_bit_binary_string(message)
binary_with_separators_list = create_binary_list_with_separators(binary_string)
print(create_unary_string(binary_with_separators_list))