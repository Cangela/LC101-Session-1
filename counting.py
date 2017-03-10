t1 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc accumsan"
t2 = "sem ut ligula scelerisque sollicitudin. Ut at sagittis augue. Praesent quis"
t3 = "rhoncus justo. Aliquam erat volutpat. Donec sit amet suscipit metus, non"
t4 = "lobortis massa. Vestibulum augue ex, dapibus ac suscipit vel, volutpat"
t5 = "eget massa. Donec nec velit non ligula efficitur luctus."

text = t1 + ' ' + t2 + ' ' + t3 + ' ' + t4 + ' ' + t5

char_count = {}
for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
keys = char_count.keys()

for char in keys:
    print(char +": " + str(char_count[char]))
print(char_count)
