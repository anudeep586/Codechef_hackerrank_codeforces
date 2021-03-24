str1=list(input())
l=[]
m=[]
flag=0
for i in str1:
    if i not in l:
        l.append(i)
for i in l:
    m.append(str1.count(i))
for i in range(len(m)-1):
    if m[i]==m[i+1]:
        flag=flag+1
if (flag+1)==len(m):
    print("YES")
else:
    last=[]
    for j in l:
        str1.remove(j)
        k=[]
        mko=0
        lk=[]
        for lkj in str1:
            if lkj not in lk:
                lk.append(lkj)
        for z in lk:
            k.append(str1.count(z))
        for lop in range(len(k)-1):
            if k[lop]==k[lop+1]:
                mko=mko+1
        if (mko+1)==len(k):
            last.append("YES")
            break;
        else:
            str1.append(j)
            last.append("NO")
    if "YES" in last:
        print("YES")
    else:
        print("NO")

            
            
