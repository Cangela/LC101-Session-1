def rotate(n,s):

    x, z = len(s), n % len(s)

    new_str = ''
    r_str = ''
    if z > 0:

        for i in range(z, x):

            new_str +=  s[i]
        #print(new_str)

        for j in range(z):
            r_str += s[j]
            #print(r_str)

        return new_str + r_str
    else:
        return s
def main():

    print(rotate(4, 'dragonfly'))
    print(rotate (3, 'good morning'))
    print(rotate(2, 'good morning'))
    print(rotate(36, 'dragonfly'))

if __name__ == '__main__':
    main()
