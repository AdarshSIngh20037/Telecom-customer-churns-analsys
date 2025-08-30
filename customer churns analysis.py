#!/usr/bin/env python
# coding: utf-8

# In[21]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


df = pd.read_csv("Customer Churn.csv")


# In[4]:


df


# In[5]:


df.info()


# In[6]:


df['TotalCharges'] = df['TotalCharges'].replace(" ", "0")
df['TotalCharges'] = df['TotalCharges'].astype ("float")


# In[7]:


df.info()


# In[8]:


df.isnull().sum().sum()


# In[9]:


df.describe()


# In[10]:


df.duplicated().sum()


# In[11]:


def conv(value):
    if value ==1:
        return "yes"
    else:
        return "no"
    
df['SeniorCitizen']= df['SeniorCitizen'].apply(conv)


# In[12]:


df.head(40)


# In[53]:


ax = sns.countplot(x = "Churn", data = df)
ax.bar_label(ax.containers[0]) 
plt.title("customer by churns")


# In[58]:


plt.figure(figsize=(3,4))
gf=df.groupby("Churn").agg({"Churn":"count"})
plt.pie(gf['Churn'], labels=gf.index, autopct= "%1.2f%%")
plt.title("Percentage of churns customer", fontsize ="10")


# In[69]:


plt.figure(figsize = (3,3))
sns.countplot(x = 'gender',  data= df, hue="Churn")
plt.title("Churn by gender", fontsize = "12")
plt.show()


# In[71]:


plt.figure(figsize = (3,3))
sns.countplot(x = 'SeniorCitizen',  data= df, hue="Churn")
plt.title("Churn by SeniorCitizen", fontsize = "8")
plt.show()


# In[74]:


import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import pandas as pd

# Crosstab to count churn per SeniorCitizen
ct = pd.crosstab(df['SeniorCitizen'], df['Churn'])

# Convert counts to percentages
ct_percent = ct.div(ct.sum(axis=1), axis=0) * 100

# Plot stacked bar chart
ax = ct_percent.plot(kind='bar', stacked=True, figsize=(4,4), colormap="Set2")

# Add percentage labels on each segment
for c in ax.containers:
    ax.bar_label(c, fmt='%.1f%%', label_type='center')

plt.title("Churn by SeniorCitizen (%)", fontsize=10)
plt.xlabel("Senior Citizen (0 = No, 1 = Yes)")
plt.ylabel("Percentage %")
plt.legend(title="Churn")
plt.show()


# In[79]:


plt.figure(figsize = (9,4))
sns.histplot(x='tenure', data = df, bins= 50, hue= "Churn")
plt.show()


# In[85]:


plt.figure(figsize = (6,6))
ax=sns.countplot(x = 'Contract',  data= df, hue="Churn")
ax.bar_label(ax.containers[0])
plt.title("Churn by Contract", fontsize = "15")
plt.show()


# In[86]:


df.columns.values


# In[88]:


cols = [
    'PhoneService', 'MultipleLines', 'InternetService',
    'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
    'TechSupport', 'StreamingTV', 'StreamingMovies'
]

# Set up subplot grid (3 rows, 3 cols)
fig, axes = plt.subplots(3, 3, figsize=(15, 12))

# Flatten axes for easy iteration
axes = axes.flatten()

# Loop through columns and create countplots
for i, col in enumerate(cols):
    sns.countplot(x=col, data=df, ax=axes[i], palette="Set2", hue = "Churn")
    axes[i].set_title(f"Count of {col}", fontsize=12)
    axes[i].tick_params(axis='x', rotation=30)

# Adjust layout
plt.tight_layout()
plt.show()


# In[94]:


plt.figure(figsize = (5,5))
ax=sns.countplot(x = 'PaymentMethod',  data= df, hue="Churn")
ax.bar_label(ax.containers[0])
ax.bar_label(ax.containers[1])
plt.title("Churn by PaymentMethod", fontsize = "10")
plt.xticks(rotation = 45)
plt.show()


# In[ ]:




