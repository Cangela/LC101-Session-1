def is_palindrome(s):
    rev = ''
    for ch in s:
        rev = ch + rev
    print(rev)
    if s == rev:
        return 'true'
    else:
        return 'false'

def main():
    t = 'racecar'
    print(t, is_palindrome(t))
    q = 'stop spit smart on no trams tips pots'
    print(q, is_palindrome(q))

if __name__ == '__main__':
    main()
