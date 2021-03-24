N,Q=[int(x) for x in input().split(" ")]
A=list(map(int,input().rstrip().split()))
p=[2]
jkl=3
while True:
    m=0
    for i in range(2,jkl):
        if (jkl%i)==0:
            m=1
            break
    if m!=1:
        if len(p)==Q:
            break
        p.append(jkl)
    else:
        jkl=jkl+1
z=[]
for q in range(Q):
    A1=[]
    B=[]
    for gjf in A:
        km=A.pop()
        if km%p[q]==0:
            B.append(i)
        else:
            A1.append(i)
    for i in A1:
        A.append(i)
    z.append((B))
z.append((A))
print(A)
print(z)
for x in z:
    for r in x:
        print(x.pop())
        
        
        
