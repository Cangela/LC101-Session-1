def rotate(n,s):

    x, z = len(s), n % len(s)

    if z > 0:
        return s[z:x] + s[:z]

    else:
        return s

def main():

    print(rotate(4, 'dragonfly'))
    print(rotate (3, 'good morning'))
    print(rotate(2, 'good morning'))
    print(rotate(36, 'dragonfly'))

if __name__ == '__main__':
    main()
