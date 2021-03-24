tests=int(input())
stack=[]
arr=[]
z=[]
for _ in range(tests):
    arr1=list(map(str,input().rstrip().split()))
    op=int(arr1[0])
    if op==1:
        stack1=[]
        for j in (stack):
            stack1.append(j)
        arr.append(stack1)
        w=arr1[1]
        for i in range(len(w)):
            stack.append(w[i])
    elif op==2:
        stack1=[]
        for j in (stack):
            stack1.append(j)
        arr.append(stack1)
        w=int(arr1[1])
        for i in range(int(w)):
            stack.pop()
    elif op==3:
        w=int(arr1[1])
        z.append((stack[w-1]))
    elif op==4:
        stack=arr.pop()
for x in z:
    print(x)
        
    
