t = "aaabbbbbcddeeeeeeeeeeee ff g hhhhh iiiikklll mmmm ppp!!!"
text = t.lower()
char_count = {}
for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
keys = char_count.keys()
keys.sort()
for char in keys:
    print(char +": " + str(char_count[char]))
print(char_count)
