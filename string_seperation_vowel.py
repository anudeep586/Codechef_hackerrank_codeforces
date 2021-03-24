a="asdef edfgh iodfk sdfd asdef eiod"
res=[]
s=""
for i in range(len(a)):
    if a[i]==" ":
        if s[0]=="a" or s[0]=="e" or s[0]=="i" or s[0]=="o" or s[0]=="u":
            res.append(s)
            s=""
        else:
            s=""
    else:
        s=s+a[i]
if s[0]=="a" or s[0]=="e" or s[0]=="i" or s[0]=="o" or s[0]=="u":
    res.append(s)
    print(*res)
else:
    print(*res)
    
