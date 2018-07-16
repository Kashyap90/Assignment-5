
# coding: utf-8

# In[1]:


(x, y) = (5, 0)
try:
    z = x/y
except ZeroDivisionError as e:
    z = e
print(z)

