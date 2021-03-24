try:
    tests=int(input())
    l=[]
    for _ in range(tests):
        x,y=[int(x) for x in input().split(" ")]
        z=[]
        k=[]
        if x==1:
            z.append(0)
            if len(z)<=y:
                l.append("Chef")
            else:
                l.append("Divyam")
        else:
            for i in range(2,x+1):
                m=0
                for j in range(2,i+1):
                    if i!=j:
                        if i%j==0:
                            m=1
                            break
                if m!=1:
                    k.append(i)
            if len(k)<=y:
                l.append("Chef")
            else:
                l.append("Divyam")
    for x in l:
        print(x)
except:pass
                            
                            
                        
                    
                    
                
