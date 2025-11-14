r=5
c=10
for i in range(r):
    for j in range(c):
        if i==0 or i==r-1 or j==0 or j==c-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()  

# r=5
# c1=r-1
# c2=3
# for i in range(r):
#     for j in range(c1-i):
#         print(' ',end='')
#     for k in range(c2):
#         print('*',end='')

#     print()
# for f in range(r):
#     for g in range(f+1):
#         print(' ',end='')
#     for h in range(c2):
#         print('*',end='')
#     print()