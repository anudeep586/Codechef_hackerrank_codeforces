try:
    arr=['b', 'd', 'f', 'h', 'j', 'l', 'n', 'p', 'r', 't', 'v', 'x', 'z']
    str1=list(input())
    tests=int(input())
    z=[]
    for _ in range(tests):
        x,y=[int(asd) for asd in input().split(" ")]
        x=x-1
        l=str1[x:y]
        res=[]
        count=0
        for i in l:
            if i not in res:
                res.append(i)
                if i in arr:
                    count=count+1
        z.append(count)
    for x in z:
        print(x)
except:pass
    
