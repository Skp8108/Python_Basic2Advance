#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Range in Python # range is a collection
# range()
# range(stop)
# range(start,stop)
# range(start,stop,step)
print(range(10))
print(range(1,10))
print(range(1,10,2))


# In[1]:


#Loop in python
# for loop and while loop
# syntax of for loop
# for object in collection:
    #logic [loop body finish then only else part will be executed]
# else: # it is optional
    #logic
#for loop example
#program1
print("For loop Example")
for x in range(10):
    print(x,end=' ')
else:
    print("Thanks")
    
#program2
for x in range(2,21,2):
    print(x,end=' ')
else:
    print("Thanks")


# In[5]:


#Q 
#   1  
#   121  
#   12321  
#   1234321  
#   123454321 
print("***Pattern***")
i=1
j=1
for x in range(5):
    print(i)
    j=j*10+1
    i=j*j


# In[13]:


#Q print 1 to 10 with total sum of table
sum=0
for x in range(1,11):
    print(x)
    sum +=x
else:
    print("Sum of Table is:- ",sum)
    


# In[4]:


#Nested Loop [Loop within Loop]
#for
  #for
for x in range(1,5): #outer loop
    for y in range(1,10): #inner loop
        print(y,end='')
    else:
        print()


# In[7]:


#Q 
#  1
#  12
#  123
#  1234
#  12345
for x in range(1,6):
    for y in range(1,x+1):
        print(y,end=' ')
    else:
        print()


# In[8]:


print('*'*5)


# In[9]:


#Q 
# *
# ***
# *****
# *******
# *********
for x in range(1,10,2):
    print('*'*x)


# In[11]:


# Q
#     *
#    ***
#   *****
#  *******
# *********
s=5
for x in range(1,10,2):
    print(' '*s,end='')
    print('*'*x)
    s -=1


# In[14]:


# Q
#     *
#    ***
#   *****
#  *******
# *********
s=5
for x in range(1,10,2):
    for y in range(s):
        print(end=' ')
    print('*'*x)
    s -=1


# In[ ]:




