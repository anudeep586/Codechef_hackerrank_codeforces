try:
    tests=int(input())
    mk=[]
    for _ in range(tests):
        length=int(input())
        a=11
        k=a
        z=[]
        b=[0]
        for i in range(length+2):
            b.append(10)
        for j in range(length):
            a=a+j
            s=""
            for i in range(length):
                a=a+b[i]
                s=str(s)+str(a)
            a=k
            z.append(s)
        mk.append(z)
    for x in range(len(mk)):
        for j in range(len(mk[x])):
            print(mk[x][j])
except:pass
        
