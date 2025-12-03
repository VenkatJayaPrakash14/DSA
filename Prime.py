def prime(num):
    if num==1 or num==0:
        return False
    for i in range(2,num+1):
        if num%2==0:
            return False
        else:
            return True
print(prime(76))