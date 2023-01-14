#!/usr/bin/env python
# coding: utf-8

# In[5]:


n=int(input("Enter a positive integer :"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")


# In[ ]:





# In[ ]:




