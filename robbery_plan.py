try:
    tests=int(input())
    p=[]
    for _ in range(tests):
        X,Y=[int(x) for x in input().split(" ")]
        A,B=[int(x) for x in input().split(" ")]
        N,M=[int(x) for x in input().split(" ")]
        z=[0]
        k=[0]
        a=0
        b=0
        for i in range(A+1):
            for j in range(B+1):
                if i*N+j*M<=X:
                    if i+j not in z:
                        a=i
                        b=j
                        z.append(i+j)
                elif i*N+j*M>X:
                    break
        A=A-a
        B=B-b
        for i in range(A+1):
            for j in range(B+1):
                if i*N+j*M<=Y:
                    if i+j not in k:
                        k.append(i+j)
                elif i*N+j*M>Y:
                    break
        l=z[-1]+k[-1]
        p.append(l)
    for x in p:
        print(x)
except:pass
        
