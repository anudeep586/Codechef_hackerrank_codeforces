tests=int(input())
z=[]
for i in range(tests):
    length=int(input())
    l=[-1]
    if length%3==0 and length%5!=0:
        a='5'
        l[0]=int(a*length)
        asd=l[0]
        l.append(asd)
    if length%5==0 and length%3!=0:
        b='3'
        l[0]=int(b*length)
        asd=l[0]
        l.append(asd)
    if length%5==0 and length%3==0:
        a='5'
        l[0]=int(a*length)
        asd=l[0]
        l.append(asd)
    if length>=3:
        k=[-1]
        for i in range(1,length):
            ab=length-(5*i)
            if ab%3==0 and ab>0:
                ac=5*i
                k[0]=int(('5'*ab)+('3'*ac))
                asdf=k[0]
                k.append(asdf)
                break;
        if int(l[0])<=int(k[0]):
            z.append(k[0])
        elif int(l[0])>int(k[0]):
            z.append(l[0])
    else:
        z.append("-1")
for x in z:
    print(x)
