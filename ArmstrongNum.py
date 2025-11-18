num=int(input('enter num  '))
sum=0
n=len(str(num))
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**n
    temp=temp//10
if num==sum:
    print('armstromg')
else:
    print('not a armstrong')
