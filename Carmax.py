#!/usr/bin/env python
# coding: utf-8

# # Carmax Analytics Competition 

# In[172]:


import pandas as pd
import random
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
import numpy as np


# In[3]:


df = pd.read_csv("C:/Users/msado/Documents/CarMax.csv") 
df2 = pd.read_excel("C:/Users/msado/Documents/national_M2019_dl.xlsx")


# In[173]:


print(df.dtypes)


# ## Create Unique variables 

# In[203]:


jobs = df2['occ_title']
median_salary = df2['a_median']
annual_bottom = df2['a_pct10']
cust_income = df['customer_income']
cust_age = df['customer_age']
vehicle_cost = df['purchase_price']
distance = df['customer_distance_to_dealer']


# ## Cleaning up distance to dealership

# In[207]:


distance_range = set()
for num in distance:
    if num == '?':
        continue
    parts1 = num.split("-")
    if len(parts1) == 2:
        distance_range.add((int(parts1[0]))
#distance_range= list(distance_range)
distance_range.sort()
distance_range



'''
new_purchase_prices = set()
for num in vehicle_cost:
    if num == '?':
        continue
    parts1 = num.split("-")
    if len(parts1) == 2:
        new_purchase_prices.add((int(parts1[0]),int(parts1[1])))
    else:
        new_purchase_prices.add((int(parts1[0][:-1])))
new_purchase_prices= list(new_purchase_prices)
new_purchase_prices.sort()
# Removing age ranges above 100's as it could mean fraud 
new_purchase_prices
'''


# In[ ]:


new_prices = []

for i in range(len(vehicle_cost)):
    if vehicle_cost[i] == '?':
        y = random.randint(0,len(new_purchase_prices)- 1)
        new_prices.append( '%d - %d'%(new_purchase_prices[y][0],new_purchase_prices[y][1]) )
    else:
        new_prices.append(vehicle_cost[i])
        
df['new_prices']= new_prices


# In[ ]:


fig, ax = plt.subplots()
ax.hist(df['new_prices'], color = 'g',bins = 40)

fig.suptitle('Count of Vehicle Purchase Ranges')
fig.set_size_inches(15,8)

ax.xaxis.set_label_text('Vehicle Price Ranges')
ax.xaxis.set_tick_params(which = 'both', top = False, bottom = True, labelbottom = True)  # Turn top x axis tick marks off 

ax.yaxis.set_label_text('Total Vehicle Price Range Totals')
ax.yaxis.set_tick_params(which = 'both', right = False, left = True, labelleft = True)   # Turn right y axis tick marks off


plt.style.use('ggplot')
ax.set_xlim(0,10)
ax.set_ylim(0,90000)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.grid(False)


# In[ ]:





# ## Cleaning up Vehicle Purchase Price 

# In[ ]:


Car_purchase = np.random.choice(1, 18, p =[0.025598948,
0.284308491,
0.332151267,
0.186417103,
0.09084676,
0.042894395,
0.020431389,
0.008601359,
0.004425724,
0.001910789,
0.001048124,
0.000584477,
0.000382158,
0.000179839,
0.000112399,
3.93398E-05,
4.77697E-05,
1.12399E-05,
8.42995E-06,
]) 


# In[198]:


new_purchase_prices = set()
for num in vehicle_cost:
    if num == '?':
        continue
    parts1 = num.split("-")
    if len(parts1) == 2:
        new_purchase_prices.add((int(parts1[0]),int(parts1[1])))
    else:
        new_purchase_prices.add((int(parts1[0][:-1])))
new_purchase_prices= list(new_purchase_prices)
new_purchase_prices.sort()
# Removing age ranges above 100's as it could mean fraud 
new_purchase_prices


# In[179]:


new_prices = []

for i in range(len(vehicle_cost)):
    if vehicle_cost[i] == '?':
        y = random.randint(0,len(new_purchase_prices)- 1)
        new_prices.append( '%d - %d'%(new_purchase_prices[y][0],new_purchase_prices[y][1]) )
    else:
        new_prices.append(vehicle_cost[i])
        
df['new_prices']= new_prices


# In[211]:


fig, ax = plt.subplots()
ax.hist(df['new_prices'], color = 'g',bins = 40)

fig.suptitle('Count of Vehicle Purchase Ranges')
fig.set_size_inches(15,8)

ax.xaxis.set_label_text('Vehicle Price Ranges')
ax.xaxis.set_tick_params(which = 'both', top = False, bottom = True, labelbottom = True)  # Turn top x axis tick marks off 

ax.yaxis.set_label_text('Total Vehicle Price Range Totals')
ax.yaxis.set_tick_params(which = 'both', right = False, left = True, labelleft = True)   # Turn right y axis tick marks off


plt.style.use('ggplot')
ax.set_xlim(0,10)
ax.set_ylim(0,130000)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.grid(False)


# ## Clean up the customer ages

# In[124]:


age_ranges = set()
for num in cust_age:
    if num == '?':
        continue
    parts1 = num.split("-")
    if len(parts1) == 2:
        age_ranges.add((int(parts1[0]),int(parts1[1])))
    else:
        age_ranges.add((int(parts1[0][:-1]),110))
age_ranges= list(age_ranges)
age_ranges.sort()
# Removing age ranges above 100's as it could mean fraud 
del age_ranges[9]
age_ranges


# In[177]:


new_ages = []

for i in range(len(cust_age)):
    if cust_age[i] == '?':
        y = random.randint(0,len(age_ranges)- 1)
        new_ages.append( '%d - %d'%(age_ranges[y][0],age_ranges[y][1]) )
    else:
        new_ages.append(cust_age[i])
        
df['new_ages']= new_ages


# In[171]:


fig, ax = plt.subplots()
ax.hist(df['new_ages'], color = 'g',bins = 20)

fig.suptitle('Count of Customer ages')
fig.set_size_inches(11,5)

ax.xaxis.set_label_text('Customer Age Ranges')
ax.xaxis.set_tick_params(which = 'both', top = False, bottom = True, labelbottom = True)  # Turn top x axis tick marks off 

ax.yaxis.set_label_text('Total Age Range Totals')
ax.yaxis.set_tick_params(which = 'both', right = False, left = True, labelleft = True)   # Turn right y axis tick marks off


plt.style.use('ggplot')
ax.set_xlim(0,10)
ax.set_ylim(0,90000)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.grid(False)


# ## Want to rearrange the data so that income doesn't include dashes

# In[129]:


income_ranges = set()
for val in cust_income:
    if val == '?':
        continue 
    parts = val.split('-')
    #print(parts)
    if len(parts) == 2:
        income_ranges.add((int(parts[0]),int(parts[1])))
    else:
        income_ranges.add((int(parts[0][:-1]),1000001))
income_ranges= list(income_ranges)

income_ranges.sort()
income_ranges


# ### Give values to the "?" in the data set

# In[216]:


len(probs)


# In[217]:


# Using choice() method 
probs = [0.091754385,0.2272012,0.216433344,0.11958165,0.083268235,0.044451126,0.020959665,0.021260334,0.010551487,0.004639282,0.030645678,0.129253612]

new_income = []

for i in range(len(cust_income)):
    if cust_income[i] == '?':
        #x = random.randint(0,len(income_ranges)- 1)
        pick1 = np.random.choice(12, 45998, p = probs) 
        new_income.append( '%d - %d'%(income_ranges[pick1][0],income_ranges[pick1][1]) )
    else:
        new_income.append(cust_income[i])
        
df['new_income']= new_income


# ###  Plot Distributions

# In[161]:


fig, ax = plt.subplots()
ax.hist(df['new_income'], color = 'Gold',bins = 23)

fig.suptitle('End of Year test Score Frequency Histogram')
fig.set_size_inches(20,10)

ax.xaxis.set_label_text('Customer Income Ranges')
ax.xaxis.set_tick_params(which = 'both', top = False, bottom = True, labelbottom = True)  # Turn top x axis tick marks off 

ax.yaxis.set_label_text('Total Income Range Totals')
ax.yaxis.set_tick_params(which = 'both', right = False, left = True, labelleft = True)   # Turn right y axis tick marks off
abline =True 
ax.set_ylim(0,100000)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.grid(False)


# ## Incoprating BLS jobs data with customer income

# In[219]:


v1 = {}
for i in range(len(annual_bottom)):
    try:
        bottom = int(annual_bottom[i])
        if bottom < 21000:
            if v1.get(20000) is None:
                v1[20000] = [ jobs[i] ]
            else:
                v1[20000].append(jobs[i])
    except: 
        pass
        
for i in range(len(median_salary)):
    for low,high in income_ranges:
        try:
            salary = int(median_salary[i])
            if salary >= low and salary <= high:
                if v1.get(high) is None:
                    v1[high] = [ jobs[i] ]
                else:
                    v1[high].append( jobs[i] )
        except: 
            pass

v1


# ## See who pursued financing 

# In[163]:


fin = []
for i in range(len(df)):
    if df['vehicle_financing'][i] == 1:
        fin.append([df['new_ages'][i],df['vehicle_financing'][i],df['new_income'][i],df['purchase_make'][i]])
fin


# In[ ]:




