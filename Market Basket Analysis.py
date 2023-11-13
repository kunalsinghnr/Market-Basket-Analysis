#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

#apriori algortithm
from mlxtend.frequent_patterns import apriori

from mlxtend.frequent_patterns import association_rules


# In[2]:


import warnings
warnings.filterwarnings('ignore')


# In[3]:


import matplotlib.pyplot as plt


# In[4]:


df = pd.read_excel('C:\\Users\\kunal.singh\\Desktop\\Learnings\\datasets\\online_retail_II.xlsx')


# In[5]:


df.head()


# <h4> <center> Data Audit

# In[6]:


df.head()


# In[7]:


df.shape


# In[8]:


df.tail()


# In[9]:


df['Country'].value_counts().head()


# In[10]:


df.info()


# In[11]:


df.isnull().sum()


# In[12]:


#cleaning up spaces in description

df['Description'] = df['Description'].str.strip()


# In[13]:


df.head()


# In[14]:


#dropping null values from the dataset

df.dropna(axis= 0, subset = ['Customer ID'] , inplace = True)


# In[15]:


df.isnull().sum()


# In[16]:


df.shape


# In[17]:


df.info()
#invoice column contains invoices that is cancelled starting with c hence we would remove those columns


# In[18]:


#convert invoice to string and removing the data starting with C

df['Invoice'] = df['Invoice'].astype(str)
df = df[~df['Invoice'].str.contains('C')] #goal was to remove cancelled invoices


# In[19]:


df.shape


# ---

# In[20]:


#picking countries and doing a country specific analysis - Picked France

basket = (df[df['Country']=='France'].groupby(['Invoice','Description'])['Quantity'].sum().unstack().reset_index().fillna(0).set_index('Invoice'))


# In[21]:


basket.head()


# In[22]:


basket.shape #shape of the dataset


# In[23]:


basket


# In[24]:


#we need to convert the values of the basket table to 0 and 1 to identify they are bought and not bought

def ecode_units(x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1


# In[25]:


basket_sets = basket.applymap(ecode_units)


# In[26]:


basket_sets


# <h3> Applying Apriori Algorithm - France

# In[27]:


#building a list of frequently bought items

frequent_itemsets = apriori(basket_sets, min_support= 0.05, use_colnames = True)


# In[28]:


frequent_itemsets


# In[29]:


rules = association_rules(frequent_itemsets, metric = 'lift',  min_threshold = 1 )


# In[30]:


rules


# In[31]:


#deriving the final list of items 
rules[(rules['lift'] >= 6) & (rules['confidence'] >= 0.8)] #there items have the highest association with one another in France


# ---

# In[32]:


# Germany basket

basket_g = (df[df['Country']=='Germany'].groupby(['Invoice','Description'])['Quantity'].sum().unstack().reset_index().fillna(0).set_index('Invoice'))


# In[33]:


basket_g


# In[34]:


basket_g.head()


# In[35]:


#we need to convert the values of the basket table to 0 and 1 to identify they are bought and not bought

def ecode_units_g(x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1


# In[38]:


basket_sets_g = basket_g.applymap(ecode_units_g)


# In[39]:


basket_sets_g


# <h3> Applying Apriori Algorithm - Germany
#     

# In[40]:


#building a list of frequently bought items

frequent_itemsets_g = apriori(basket_sets_g, min_support= 0.05, use_colnames = True)


# In[41]:


frequent_itemsets_g


# In[42]:


rules_g = association_rules(frequent_itemsets_g, metric = 'lift',  min_threshold = 1 )


# In[43]:


rules_g


# In[44]:


#deriving the final list of items 
rules_g[(rules_g['lift'] >= 6) & (rules_g['confidence'] >= 0.8)] #there items have the highest association with one another in Germany


# In[ ]:




