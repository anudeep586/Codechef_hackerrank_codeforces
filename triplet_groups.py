from itertools import permutations 
try:
    tests=int(input())
    l=[]
    for _ in range(tests):
        z=[]
        k=[]
        length=int(input())
        arr=list(map(int,input().rstrip().split()))
        res=permutations(arr,3)
        res1=[list(x) for x in res]
        for i in res1:
            f=sum(i)
            if f%3==0:
                for j in i:
                    z.append(j)
        for i in z:
            if i not in k:
                k.append(i)
        k=sorted(k)
        l.append(k)
    for o in l:
        print(*o)
except:pass
                
                
            
         
