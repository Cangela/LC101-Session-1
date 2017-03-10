####initials.py####

def get_initials(fullname):

    name_cap = fullname.upper()
    names = name_cap.split()
    init = ""
    for aname in names:
        init += aname[0]

    return init

def main():

    name = input("What is your full name?\n")
    print(get_initials(name))

if __name__ == '__main__':
    main()
