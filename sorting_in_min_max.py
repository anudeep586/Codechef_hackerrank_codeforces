try:
    tests=int(input())
    k=[]
    for _ in range(tests):
        length=int(input())
        arr=list(map(int,input().rstrip().split()))
        z=[]
        while True:
            if length%2==0:
                a=max(arr)
                c=min(arr)
                arr.remove(a)
                arr.remove(c)
                z.append(a)
                z.append(c)
                if len(arr)==0:
                    break
            else:
                a=max(arr)
                arr.remove(a)
                z.append(a)
                if len(arr)==0:
                    break
                c=min(arr)
                arr.remove(c)
                z.append(c)
                if len(arr)==0:
                    break
        k.append(z)
    for x in k:
        print(*x)
except:pass
        
                
