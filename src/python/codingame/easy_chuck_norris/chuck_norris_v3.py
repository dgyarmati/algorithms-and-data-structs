message = input()
binary_string = ""

for char in message:
    binary_string += bin(ord(char))[2:].zfill(7)

unary_string = ""
first_of_batch = True
for i in range(len(binary_string)):
    current_char = binary_string[i]    
    next_char = binary_string[i + 1] if i + 1 < len(binary_string) else None

    if current_char == "1":
        chars = "0 0" if first_of_batch else "0"
        first_of_batch = False
    elif current_char == "0":
        chars = "00 0" if first_of_batch else "0"
        first_of_batch = False

    unary_string += chars
    
    if next_char and current_char != next_char:
        unary_string += " "
        first_of_batch = True

print(unary_string)

# TODO write tests
# TODO recursive version
# TODO write blog post?
# TODO rewrite in C and Java