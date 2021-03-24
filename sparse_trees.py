arr=[]
arr1=[]
z=[]
tests=int(input())
for _ in range(tests):
    n=input()
    arr.append(n)
tests1=int(input())
for u in range(tests1):
    n1=input()
    arr1.append(n1)
for i in range(len(arr1)):
    a=arr.count(arr1[i])
    print(a,arr1[i])
    z.append(a)
for x in z:
    print(x)
    
