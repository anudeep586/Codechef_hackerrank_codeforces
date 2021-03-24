tests=int(input())
for _ in range(tests):
    p,h,m=[int(x) for x in input().split(" ")]
    mp=list(map(int,input().rstrip().split()))
    mh=list(map(int,input().rstrip().split()))
    for i in range(len(mp)):
        if mh[i]%p!=0:
            a=mh[i]//p+1
        else:
            a=mh[i]//p
        h=h-a*mp[i]
        if h<mp[i]:
            print("NO")
            break
        if h<=0 and i+1==len(mp):
            print("YES")
            break
        elif h>=0 and i+1==len(mp):
            print("YES")
            break
        elif h<=0 and i+1!=len(mp):
            print("NO")
            break
        
    
