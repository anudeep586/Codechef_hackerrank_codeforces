try:
    tests=int(input())
    z=[]
    for _ in range(tests):
        n,k,x,y=[int(x) for x in input().split(" ")]
        if x==y:
            z.append([n,n])
        else:
            d=[]
            if x<y:
                d=[[x+n-y,n],[n,n-y+x],[y-x,0],[0,y-x]]
            else:
                d=[[n,y+n-x],[y+n-x,n],[0,x-y],[x-y,0]]
            t=d[(k-1)%4]
            z.append([t[0],t[1]])
    for x in z:
        print(*x)
except:pass
                
