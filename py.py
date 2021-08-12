#!/usr/bin/env python
# coding: utf-8

# In[13]:


with open('sayhello.txt','r') as file:
    readthis = file.readlines()
    print(readthis)   
    

    


# In[14]:


with open('sayhello.txt','w') as file:
    file.write("hello")


# In[15]:


with open('sayhello.txt','r') as file:
    readthis = file.readlines()
    print(readthis)


# In[16]:


with open('sayhello.txt','a') as file:
    file.write("this is a newline/n")
    


# In[17]:


with open('sayhello.txt','r') as file:
    readthis = file.readlines()
    print(readthis)


# # to edit a specific line

# In[19]:


with open('sayhello.txt','r') as file:
    readthis = file.readlines()
    readthis[0] = "this is an edited line\n"
    file.close()
    file = open ("sayhello.txt", "w")
    file.writelines(readthis)
    file.close


# # to see it

# In[20]:


with open('sayhello.txt','r') as file:
    readthis = file.readlines()
    print(readthis)


# In[ ]:




