s=input()
i=0
while(i<len(s)-1):
    if(s[i]==s[i+1]):
        s=s[:i]+s[i+2:]
        if(i>0):
          i=i-1
    else:
        i=i+1
if(s==""):
    print("Empty String")
else:
    print(s)
