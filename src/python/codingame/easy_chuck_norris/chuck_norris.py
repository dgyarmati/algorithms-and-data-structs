message = input()
binary_values = []

for char in message:
    # converts char to a 7 digit 0 left padded binary value
    binary_values.append('{0:07b}'.format(ord(char)))
 
# merges the list of strings into one string and browses it, updating :
# - prev which contains the last character of binary_values ('0' or '1')
# - count which contains the number of consecutive identical characters
# and printing the result gradually
prev, count = None, 0

for char in ''.join(binary_values):
    if char != prev:
        print(('0' * count) + \
        (' ' if count else '') + \
        ("00 " if char == '0' else "0 "), end='')
        count = 1
    else:
        count += 1
    prev = char

print("0" * count, end="")

