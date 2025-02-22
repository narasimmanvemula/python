s="abcd"
rev= ""
for i in range(len(s)-1,-1,-1):
    rev= rev+s[i]
if rev == s:
   print("yes")
else:
    print("no")  
    
    