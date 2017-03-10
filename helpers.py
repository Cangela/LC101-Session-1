####helpers.py####

def rotate_character(char, rot):
    import string

    alpha_lower = string.ascii_lowercase
    alpha_upper = string.ascii_uppercase

    new_index = (alphabet_position(char)+ rot) % 26

    #Check if character is uper or lowercase and assigns it to a new index
    #based on the rotation amount

    if char in alpha_lower:
        new_char = alpha_lower[new_index]
    elif char in alpha_upper:
        new_char = alpha_upper[new_index]
    else:
        new_char = char

    return new_char



def alphabet_position(letter):

    alphabet = "abcdefghijklmnopqrstuvwxyz"

#Check if letter is alphabetical and finds its 0-based index

    if letter.isalpha():
        zed = letter.lower()
        pos = alphabet.index(zed)
    else:
        pos = -1

    return pos
