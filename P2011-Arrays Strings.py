operations=["--X","X++","X--"]
ans =0 
for i in operations:
    if i=='--X' or i=='X--':
        ans-=1
    if i=='X++' or i=='++X':
        ans+=1
print(ans)