
# coding: utf-8

# In[96]:


import pandas as pd
import re


# In[97]:


def check_phno(string):
    regex = '\d[0-9\.\s\,O=\-\:\;\_]+'
    phno = []

    temp = re.findall(regex, str(string))
    if temp!=[]:
        phno.append(temp)

    real_phno = set()
    for i in phno:
        for j in i:
            if(len(j)>=10):
                real_phno.add(j)
        
    real_phno = list(real_phno)


    final_phno = []
    for i in real_phno:
        num_count = 0
        temp = ''
        for j in i:
            if j.isdigit() == True or j == 'O' or j == 'i' or j == 'I':
                num_count = num_count + 1
                if j == 'O':
                    temp = temp + '0'
                elif j == 'i' or j == 'I':
                	temp = temp + '1'
                else:
                    temp = temp + j
        if num_count == 10:
            final_phno.append(temp)

    return final_phno


# In[98]:


df = pd.read_csv("dataset_computers.csv")
df.head(10)


# In[99]:


data = df.values.tolist()


# In[100]:


has_phno = []
phno = []


# In[101]:


for i in data:
    a = check_phno(i[2])
    b = check_phno(i[5])
    c = check_phno(i[6])
    
    if a == [] and b == [] and c == []:
        has_phno.append('0')
        phno.append('-')
    else:
        has_phno.append('1')
        temp = set()
        for i in a:
            temp.add(i)
        for i in b:
            temp.add(i)
        
        for i in c:
            temp.add(i)

        temp = list(temp)
        
        temp_str = ''
        for i in temp:
            temp_str = temp_str + i + ','
        
        phno.append(temp_str)


# In[116]:


df2 = pd.DataFrame({'Has Phone Number': has_phno})
df3 = pd.DataFrame({'Phone Number': phno})


# In[117]:


df = df.join(df2)


# In[118]:


df = df.join(df3)


# In[121]:


df.to_csv('computer_final.csv')

