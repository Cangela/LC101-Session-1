def printWithFrames(s):
    border = '|' * 4 + '|'*len(s) + '|'*4

    framed = "|"*3 + ' ' + s +  ' ' + "|"*3
    print(border)
    print(framed)
    print(border)
printWithFrames('Hello, World!')
