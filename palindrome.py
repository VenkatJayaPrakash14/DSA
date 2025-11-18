num=int(input('enter num'))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum=sum*10+digit
    temp=temp//10
if num==sum:
    print('is pal')
else:
    print('not pal')