try:
    string_input = input()
    c = 0
    c1 = 0
    c2 = 0
    c3 = 0
    for i in string_input:
        if i=='U':
            c = c + 1 
        if i=='D':
            c1 = c1 + 1 
        if i=='R':
            c2 = c2 + 1 
        if i=='L':
            c3 = c3 + 1
    if c==c1 and c==c1 and c==c2 and c==c3:
        print("true")
    else:
        print("false")
except:
    pass
