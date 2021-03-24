try:
    tests=int(input())
    z=[]
    for _ in range(tests):
        res=[]
        length=int(input())
        str1=list(input())
        for i in str1:
            if i not in res:
                res.append(i)
        res=sorted(res)
        z.append((''.join(res)))
    for x in z:
        print(x)
except:pass
