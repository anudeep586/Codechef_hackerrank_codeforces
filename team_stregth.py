try:
    tests=int(input())
    l=[]
    for _ in range(tests):
        z=[]
        k=[]
        n,x=[int(xm) for xm in input().split(" ")]
        for i in range(1,n+1):
            if i%x==0:
                if i<10:
                    z.append(i)
                else:
                    a=i%10
                    z.append(a)
        l.append(sum(z))
    for x in l:
        print(x)
except:pass
    
    
