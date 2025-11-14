prices=[7,1,2,4,6,5]
n=len(prices)
ans=0
for i in range(n):
    for j in range(i+1,n):
        temp=prices[j]-prices[i]
        ans=max(ans,temp)
print(ans)