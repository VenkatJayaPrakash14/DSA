prices=[7,1,2,4,6,5]
n=len(prices)
minv=prices[0]
ans=0
for i in range(1,len(prices)):
    ans=max(ans,(prices[i]-minv))
    minv=min(minv,prices[i])
print(ans)