n=int(input())
l=list(map(int,input().rstrip().split()))
base = []   
lists = [base] 
for i in range(len(l)): 
    orig = lists[:] 
    new = l[i] 
    for j in range(len(lists)): 
        lists[j] = lists[j] + [new] 
    lists = orig + lists
lists.remove(lists[0])
z=[]
for i in range(len(lists)):
    for j in range(len(lists)):
        if i!=j:
            m=0
            for k in (lists[j]):
                if k in lists[i]:
                    m=1
                    break
            if m!=1:
                z.append(sum(lists[i])+sum(lists[j]))
print(max(z))
                
            
