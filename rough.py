# r=10
# c=5
# for i in range(r):
#     for j in range(c):
#         if i==0 or i==r-1 or j==0 or j==c-1:
#             print('*',end='')
#         else:
#             print(' ',end='')
#     print()


r=5
c1=r-1
c2=4
for i in range(r):
    for j in range(i):
        print(' ',end='')
    for k in range(c2-i):
        print('* ',end='')
    print()