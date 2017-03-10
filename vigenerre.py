####vigenere.py####

from helpers import alphabet_position, rotate_character

def encrypt(text, key):

    v_encrypted = ""
    keyLength = 0

#indexes each key character in the ciphered text and finds the 0 indexed
#alphabet position for the rotation

    for char in text:
        if char.isalpha():
            key_char = key[keyLength % len(key)]
            keyIdx = alphabet_position(key_char)
            v_char = rotate_character(char, keyIdx)
            keyLength += 1
        else:
            v_char = char
        v_encrypted += v_char

    return v_encrypted

def main():

    user_txt = input("Type a message:\n")
    ciph_key = input("Encryption key:\n")

    print(encrypt(user_txt, ciph_key))

if __name__ == '__main__':
    main()
