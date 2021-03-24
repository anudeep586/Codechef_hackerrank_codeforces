n=int(input())
a=n^3
b=n^31
c=n^18
d=n^16
x=a & b
y=c | d
if (x==3 and y==4) or (x==15 and y==26) or (x==2 and y==11) or (x==10 and y==31):
    print("YES")
else:
    print("NO")
