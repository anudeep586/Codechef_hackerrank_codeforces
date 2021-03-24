tests=int(input())
k=[]
for ik in range(tests):
    a,b,c=[int(x) for x in input().split(" ")]
    sum1=a+b+c
    z=[]
    i=1
    for count in range(1,sum1+1):
            if i%7!=0:
                if a!=0 and a!=1:
                    a=a-1
                    i=i+1
                if b!=0 and b!=1:
                    b=b-1
                    i=i+1
                if c!=0 and c!=1:
                    c=c-1
                    i=i+1
                if a==0 and b==0 and c==0:
                    z.append("NO")
                    break;
            elif i%7==0:
                if a!=0:
                    a=a-1
                if b!=0:
                    b=b-1
                if c!=0:
                    c=c-1
                if a==0 and b==0 and c==0:
                    z.append("YES")
                    break;
                i=i+1
    if 'YES' in z:
        k.append('YES')
    elif "YES" not in z:
        k.append('NO')
for x in k:
    print(x)
            
        
