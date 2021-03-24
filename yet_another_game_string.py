tests=int(input())
z=[]
for _ in range(tests):
    s=list(input())
    l=len(s)
    for i in range(l):
        if i%2==0:
            if s[i]!='a':
                s[i]='a'
            else:
                s[i]='b'
        else:
            if s[i]!='z':
                s[i]='z'
            else:
                s[i]='y'
    z.append(s)
for x in z:
    print(''.join(x))
