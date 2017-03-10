def is_palindrome(s):

    rev = s[- 1::-1]
    if s  == rev:
        return 'true'
    else:
        #print(rev)
        return 'false'

def main():

    t = 'racecar'
    print(t, is_palindrome(t))
    q = 'stop spit smart on no trams tips pots'
    print(q, is_palindrome(q))
    z = 'crate'
    print(z, is_palindrome(z))
    x = 'ya pizza zip pizazz i pay'
    print(x, is_palindrome(x))

if __name__ == '__main__':
    main()
