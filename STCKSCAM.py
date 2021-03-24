a,c=[int(x) for x in input().split(" ")]
res = [int(x) for x in str(a)] 
for i in range(c):
    if res[i]!=9:
        res[i]=9
    else:
        i=i+1
s = ''.join(map(str, res))
print(s)
