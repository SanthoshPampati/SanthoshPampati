#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np


# In[4]:


get_ipython().system('conda install -c anaconda xlrd --yes')


# In[5]:


df = pd.read_excel('https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DV0101EN/labs/Data_Files/Canada.xlsx',sheet_name='Canada by Citizenship',
                  skiprows = range(20),skipfooter = 2)


# In[6]:


df.head()


# In[7]:


df.drop(['Type','Coverage', 'AREA', 'REG','DEV','DevName'], axis=1, inplace = True)


# In[8]:


df.rename(columns = {'OdName':'Country','AreaName':'Continent','RegName':'Region'}, inplace = True)


# In[9]:


df.head()


# In[10]:


df['Total'] = df.sum(axis = 1)


# In[11]:


df.columns.values
df.columns = list(map(str, df.columns))


# In[12]:


df.set_index('Country', inplace = True)


# In[13]:


df.head()


# In[14]:


df.isnull().sum(axis=0)


# In[16]:


df.isnull().apply(pd.Series.value_counts) # other way to find the total null cells 


# In[17]:


df.sort_values(['Total'], ascending = False, axis = 0, inplace = True)


# In[18]:


df.head()


# In[19]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib as mpl
import matplotlib.pyplot as plt


# In[20]:


years = list(map(str, range(1980,2014)))
df_top5 = df.head()
df_top5 = df_top5.loc[:,years]
df_top5t = df_top5.transpose()


# In[21]:


df_top5t.plot(kind='area', stacked = False, alpha = 0.45, figsize = (10,5))
plt.title('area plot of top5 immrigrants')
plt.xlabel('years')
plt.ylabel('num of immrigrants')
plt.show()


# In[22]:


dftotal = df['Total']
count, bin_edge = np.histogram(dftotal, bins = 15)


# In[23]:


dftotal.plot(kind='hist', xticks = bin_edge, figsize=(15,8), bins = 15)


# In[24]:


counts, bin_edge = np.histogram(df_top5)
df_top5t.plot(kind='hist',figsize = (12,8), stacked = False, alpha = 0.45, xticks = bin_edge, legend = True)


# In[128]:


df_india = df.loc['India', years]


# In[129]:


df_india.plot(kind='bar', color = 'green',figsize = (12,8))
plt.annotate('',xy=(13,23000), xytext = (9,12000), xycoords ='data', 
             arrowprops = dict(arrowstyle = '->',connectionstyle = 'arc3',lw = 0.8, color = 'red'))
plt.annotate('growth', xy = (9,13500), rotation = 55,va = 'bottom', ha = 'left')


# In[27]:


df_india = df.loc['India', years]
df_india.plot(kind='barh', color = 'lightblue',figsize = (12,8))


# In[28]:


df_Top = df['Total']


# In[ ]:





# In[ ]:





# In[37]:


df_Top = df_Top.head()


# In[38]:


df_Top.plot(kind='pie',figsize = (12,8), autopct = '%1.1f%%', pctdistance = 1.3, shadow = True)


# In[39]:


df1 = df.groupby('Continent', axis = 0).sum()


# In[40]:


df1 = df1['Total']


# In[41]:


df1.plot(kind = 'pie', shadow = True, colors = ('lightblue','green','pink','red','brown','darkred'),
        autopct = '%1.1f%%', pctdistance = 1.1, figsize = (12,10), startangle = 60,
         explode = (0,0,0,0.1,0.1,0.2), labels = None)
plt.legend(labels = df1.index)


# In[42]:


df1.plot(kind='box', )


# In[43]:


df2 = df['Total']


# In[44]:


df2.plot(kind = 'box', figsize = (12,10), color = 'red')


# In[45]:


df3 = df_top5.transpose()


# In[46]:


df3.plot(kind = 'box')


# In[133]:


df_india = df.loc[['India'],years].transpose()
df_india


# In[134]:


#df_india = pd.DataFrame({'column name':'df['column name']'})
df_india.index = list(map(int, df_india.index))


# In[135]:


df_india.reset_index(inplace = True)


# In[136]:


df_india.rename(columns = {'index':'years'}, inplace = True)


# In[137]:


df_india.drop(['level_0'], axis = 1, inplace = True)


# In[138]:


df_india.plot(kind = 'scatter', x = 'years', y = 'India', color = 'red')


# In[139]:


t = np.polyfit(x = df_india['years'],y = df_india['India'], deg = 1)
t


# In[140]:


x = df_india['years']
df_india.plot(kind = 'scatter', x = 'years', y = 'India', color = 'red')
plt.plot(x, t[0]*x + t[1], color = 'blue', marker = 'o')
plt.annotate('{0:.0f} x + {1:.0f}'.format(t[0],t[1]), xy =(2000,15000))


# In[144]:


norm_india = (df_india['India'] - df_india['India'].min()) / (df_india['India'].max() - df_india['India'].min())


# In[147]:


df_india.plot(kind = 'scatter', x = 'years', y = 'India', color = 'green',alpha = 0.4, s = norm_india*2000+10, figsize = (12,10))


# In[153]:


title_index = 0 
for col in range(40):
    #for row in range(1):
         title_index = title_index +1
            print(title_index)


# In[ ]:




