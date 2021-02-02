#Q  Homework 
#     1
#    121
#   12321
#  1234321
# 123454321
#  1234321
#   12321
#    121
#     1
i=1
j=1
s=5
for x in range(5):
    print(' '*s,end='')
    print(i)
    j=j*10+1
    i=j*j
    s -=1
i=1
j=j//100
s=2
for x in range(4):
    print(' '*s,end='')
    i=j*j
    print(i)
    j=j//10
    s +=1
