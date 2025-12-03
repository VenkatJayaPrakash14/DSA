def replaceElements(arr):
        n=len(arr)
        rmax=-1
        for i in range(n-1,-1,-1): 
            temp=arr[i]
            arr[i]=rmax
            rmax=max(rmax,temp)   
        return arr
print(replaceElements([17,18,5,4,6,1]))