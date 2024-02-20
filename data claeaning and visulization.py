#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import numpy as py
import matplotlib.pyplot as plt


# In[2]:


df=pd.read_csv(r"C:\Users\ee\OneDrive\Desktop\i221921 assigment2\earth_surface_temperatures.csv")


# In[3]:


df.head()


# In[4]:


#(a)


# In[5]:


df.isnull().sum()


# In[6]:


tm=df['Temperature'].mean()
df['Temperature'].fillna(tm,inplace=True)


# In[7]:


tmv=df['Monthly_variation'].mean()
df['Monthly_variation'].fillna(tmv,inplace=True)


# In[8]:


ta=df['Anomaly'].mean()
df['Anomaly'].fillna(ta,inplace=True)


# In[9]:


#(b)


# In[10]:


types=df.dtypes
types


# In[11]:


df['Country']=df['Country'].astype('string')
df


# In[12]:


#(c)


# In[ ]:





# In[13]:


#(d)


# In[14]:


sns.boxplot(x=df['Temperature'])
plt.show()


# In[15]:


#(e)


# In[16]:


df['Temperature'].describe()


# In[17]:


df['Monthly_variation'].describe()


# In[18]:


df['Anomaly'].describe()


# In[19]:


#(f)


# In[20]:


df["Country"].unique()


# In[21]:


df.groupby('Country').mean()
df


# In[22]:


#(g)


# In[ ]:


sns.relplot(x='Years',y='Temperature',hue='Country',data=df)
plt.show()


# In[ ]:


#(h)


# In[ ]:


ma=df['Temperature'].max()

df[df['Temperature']==ma]


# In[ ]:


mi=df['Temperature'].min()
df[df['Temperature']==mi]


# In[ ]:


#(i)


# In[ ]:


maa=df['Anomaly'].max()

df[df['Anomaly']==maa]


# In[ ]:


mii=df['Anomaly'].min()
df[df['Anomaly']==mii]


# In[ ]:


#(k)


# In[ ]:


corrt = df.corr(method = 'pearson')
corrt


# In[ ]:


sns.scatterplot(data=df, x='Temperature', y='Anomaly')


# In[ ]:


#(j)


# In[ ]:


df2=pd.read_csv(r"C:\Users\ee\OneDrive\Desktop\i221921 assigment2\earth_surface_temperatures.csv")


# In[ ]:


df2.groupby('Country')
df2.set_index('Country')


# In[ ]:


data = {
    'Date': pd.date_range(start='2000-01-01', periods=100, freq='Y'),
    'US_Temperature': [x for x in range(100)],
    'Canada_Temperature': [x for x in range(100, 200)],
    'UK_Temperature': [x for x in range(200, 300)],
    'Australia_Temperature': [x for x in range(300, 400)],
    'India_Temperature': [x for x in range(400, 500)]
}

df = pd.DataFrame(data)

df.set_index('Date', inplace=True)

plt.figure(figsize=(12, 6))
for country in df.columns:
    plt.plot(df.index, df[country], label=country)

plt.title('Temperature Trends Over the Years')
plt.xlabel('Year')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid(True)
plt.show()


# In[ ]:





# In[ ]:




