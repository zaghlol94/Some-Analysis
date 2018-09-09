
# coding: utf-8

# In[198]:


import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
sns.set_style('whitegrid')


# In[199]:


df = pd.read_excel('file.xlsx', sheet_name='Sheet1')


# In[200]:


df.head()


# In[201]:


df


# In[202]:


df = df.dropna()
df


# In[203]:


df.info()


# In[204]:


df.describe()


# In[205]:


df['Difficulty'].value_counts()


# In[206]:


fig, ax = plt.subplots(figsize=(12,6))
sns.countplot(ax=ax,x='Difficulty',data=df)


# In[207]:


fig, ax = plt.subplots(figsize=(12,6))
sns.countplot(ax=ax,x='Difficulty',data=df,hue='Est. time per day')


# In[208]:


def val (vd):
    num=vd
    if (num <=5).bool():
        return 'low'
    elif (num >5).bool() and (num <=7).bool() :
        return 'medium'
    else :
        return 'hight'


# In[209]:


df['Value']=df[['Value added (1-10)']].apply(val,axis=1)


# In[210]:


df.head()


# In[211]:


for_pie_chart = df['Value'].value_counts()


# In[212]:


fig, ax = plt.subplots(figsize=(12,6))
sns.countplot(ax=ax,x='Value',data=df)


# In[213]:


type (for_pie_chart)


# In[214]:


for_pie_chart


# In[215]:


pie_value_list = for_pie_chart.tolist()


# In[216]:


pie_label_list=['hight','low','medium']


# In[217]:


pie_list 


# In[218]:


pie_type_list


# In[219]:


plt.axis("equal")
plt.pie(pie_value_list,labels=pie_label_list,radius=1.5,autopct='%0.2f%%',shadow = True,startangle=45)
plt.show()


# In[220]:


plt.axis("equal")
plt.pie(pie_value_list,labels=pie_label_list,radius=1.5,autopct='%0.2f%%',shadow = True,explode=[0,0.1,0],startangle=45)
plt.show()


# In[221]:


x = df['Difficult  (1-20)']
y = df['Value added (1-10)']
z = df['ID']


# In[222]:


type (x)


# In[223]:


x = x.tolist()
y = y.tolist()
z = z.tolist()


# In[224]:


type (y)


# In[225]:


fig, ax = plt.subplots(figsize=(16,6))
ax.scatter(x, y,s=75,c='r',alpha=0.4)
plt.xlabel('Difficult  (1-20)',fontsize=30)
plt.ylabel('Value added (1-10)',fontsize=30)
plt.title('all use cases')
for i, txt in enumerate(z):
    ax.annotate(txt, (x[i], y[i]))   
plt.show()    

