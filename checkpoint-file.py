#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1. Write a Python program to read an entire text file.

#2. Write a Python program to read the first n lines of a file.

#3. Write a Python program to read the last n lines of a file.

#4. Write a Python program that takes a text file as input and returns the number of words of a given text file.

#5. (Bonus) Write a Python program to read the last n lines of a file.


# In[8]:


#quest 1
f=open("python.txt","r",encoding="utf-8")
f.read()


# In[31]:


#quest 2
f=open("python.txt","r",encoding="utf-8")
print(f.readlines()[0])


# In[30]:


#quest 3
f=open("python.txt","r",encoding="utf-8")
print(f.readlines()[-1])


# In[40]:


#quest 4 Write a Python program that takes a text file as input and returns the number of words of a given text file.
f=open("python.txt","r",encoding="utf-8")
text=f.read()
str(text)
text_2=text.split()
number_of_words = len(text_2)
print(number_of_words)


# In[ ]:




