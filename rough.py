# a=[7,1,5,4]
# minV=a[0]
# ans=0
# for i in range(1,len(a)):
#     ans=max(ans,(a[i]-minV))
#     minV=min(minV,a[i])
# print(ans)

nums = [1, 1, 2, 2, 3, 3, 4]
k = remove_duplicates(nums)

print("Count:", k)
print("Array without duplicates:", nums[:k])
