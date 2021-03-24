try:
    tests=int(input())
    l=[]
    for _ in range(tests):
        arr=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        str1=list(input())
        for i in range(len(str1)):
            str1[i]=str1[i].upper()
        key=[98,57,31,45,46]
        z=[]
        k=[]
        for i in range(len(str1)):
            a=arr.index(str1[i])
            z.append(a)
        for i in range(len(z)):
            b=key[i]+z[i]
            c=b%26
            k.append(arr[c])
        d=''.join(k)
        l.append(d)
    for x in l:
        print(x)
except:pass
        
    
