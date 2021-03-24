tests=int(input())
z=[]
for _ in range(tests):
    a,b,c,d=[int(x) for x in input().split(" ")]
    A=c+d
    B=c-d
    if d==0:
        z.append(abs(a-b))
        print("hi6")
    elif B not in range(a,b) and A not in range(a,b):
        print("hi")
        z.append(0)
    elif A in (a,b) or B in (a,b):
        if A in (a,b):
            if abs(A-a)<abs(A-b):
                fg=abs(a-b)
                print("hi1")
                z.append(abs(fg-abs(A-a)))
            if abs(A-a)>abs(A-b):
                fg=abs(a-b)
                print("hi2")
                z.append(abs(fg-abs(A-b)))
        if B in (a,b):
            if abs(B-a)<abs(B-b):
                fg=abs(a-b)
                print("hi3")
                z.append(abs(fg-abs(B-a)))
            if abs(B-a)>abs(B-b):
                fg=abs(a-b)
                print("hi4")
                z.append(abs(fg-abs(B-b)))
    if A and B in (a,b):
        if abs(a-A)<abs(b-A):
            w=abs(a-A)
        else:
            w=abs(b-A)
        if abs(a-B)<abs(b-B):
            e=abs(a-B)
        else:
            e=abs(b-B)
        print("hi5")
        z.append(w+e)
for x in z:
    print(x)
                
                
            
    
        
