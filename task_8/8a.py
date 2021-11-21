#!/usr/bin/env python
# coding: utf-8

# # note that when calling chrome the capital letter of chrome
# 

# In[33]:


from selenium import webdriver
from webdrivermanager import ChromeDriverManager


x= webdriver.Chrome(executable_path= r"C:\Users\hp\Desktop\chromedriver\chromedriver.exe")
x.get("https://github.com")
x.implicitly_wait(5)

link= x.find_element_by_link_text("Sign in")
link.click()
user = x.find_element_by_id("login_field")
user.clear()
user.send_keys("example.com")
x.implicitly_wait(5)
passwoo = x.find_elements_by_id("password")
passwoo.clear()
passwoo.send_keys("000")
x.implicitly_wait(5)
x.find_element_by_class_name("password").click()


# In[ ]:





# In[ ]:




