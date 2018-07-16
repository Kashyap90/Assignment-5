
# coding: utf-8

# In[7]:


subject=["Americans", "Indians"]
verb=["play", "watch"]
obj=["Baseball", "Cricket"]

sentence_list = [(sub+" " + vb+" "+ ob) for sub in subject for vb in verb for ob in obj]
for sentence in sentence_list:
 print (sentence)

