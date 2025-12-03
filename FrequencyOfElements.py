arr=[1,2,3,1,2,1,5,1]
dic={}
for i in arr:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]=dic[i]+1
print(dic)