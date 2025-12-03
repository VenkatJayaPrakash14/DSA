arr=[5,6,7,1,2,4,3]
n=len(arr)
for i in range(0,n-1):
    swapping=False
    for j in range(n-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
            swapping=True
    if swapping==False:
        break
print(arr)
