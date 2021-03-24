n=int(input())
str1=input()
substring = [str1[i: j] for i in range(len(str1)) 
          for j in range(i + 1, len(str1) + 1)]
z=[]
for sub in substring:
    if len(sub)==1:
        z.append(str(sub))
    if len(sub)>1 and len(sub)%2==0:
        sub1=list(sub)
        counting=sub1.count(sub1[0])
        if (counting)==len(sub1):
            z.append(str(sub))
    if len(sub)>1 and len(sub)%2!=0:
        mid=len(sub)//2
        sub1=list(sub)
        sub1.remove(sub1[mid])
        counting=sub1.count(sub[0])
        if (counting)==len(sub1):
            z.append(str(sub))
print(len(z))
        
