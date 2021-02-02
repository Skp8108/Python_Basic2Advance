#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Membership operator
#in :- it is used to to find out character from the string
#not in :- it is used in negative sense
#object-having state
#Variable:-which change 
#obj = 1234
obj1='raman'
obj2='Raman'
#print('r' in obj)#error
print('r' in obj1)
print('r' in obj2)
print('r' not in obj2)


# In[8]:


#Identity operator
#is :- it is used to identify two objects are equal or not eiter its a number or string
#is not
a=5
b=5
print(a is not b)
name='ram'
name1='ram'
print(name is name1)
name2='Ram'
print(name is not name2)


# In[ ]:


#Identifier :- it ia name of obj,class,function etc. and name is always declare with alphabet(A...Z|a...z) or underscore
#PVM(Python Virtual Machine) :- its craete a virtual memory
#Virtual Memory:-which do not exist in a system,it create at runtime by the use of ram and hard disk space


# In[10]:


#Asssignment Operators
# = Assigns values from right side operands to left side operand
# += Add equal
# -= Subtract equal
# *= Multiply equal
# /= Divide equal
# %= Modulus equal
# **= power equal
# //= Floor division equal
#we cannot use assignment operator in middle
a=10
a +=10
print(a)
a=a+10
a +=10-5
print(a)
b=2
a+=b+(3*b)
print(a)


# In[11]:


#Loop(Meaning iteration)
for x in range(10):
    print(x)


# In[14]:


#Q 54321
#  4321
#  321
#  21
#  1

#Step1. Create a loop for reverse mode 5 to 1 step -1
#step2. Create second loop for print value start from first loop value until 1
#step3. Break the line

for x in range(5,0,-1):
    for y in range(x,0,-1):
        print(y,end='')
    else:
        print()


# In[37]:


#Q  Homework  #Telegram:-9891794597
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


# In[ ]:





# In[ ]:




