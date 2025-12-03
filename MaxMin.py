def MaxMin(arr):
    MAX=arr[0]
    MIN=arr[0]
    for i in range(1,len(arr)):
        if MAX<arr[i]:
            MAX=arr[i]
        if MIN>arr[i]:
            MIN=arr[i]
    return MAX,MIN 
print(MaxMin([5,7,8,9,2,1]))