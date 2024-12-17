#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd

# Load the dataset
data = pd.read_csv('employee_burnout_analysis-AI 2.csv')  # Adjust the path accordingly
data


# ###  Inspect the Data

# In[10]:


print(data.info())
print(data.describe())


# ### Handle Missing Values

# In[11]:


data.fillna(data.mean(), inplace=True)  # For numerical columns
data.dropna(inplace=True)  # Drop rows with any missing value


# ### Convert Data Types: 
# Ensure that the data types are appropriate for analysis. For example, convert 'Date of Joining' to datetime format.

# In[12]:


data['Date of Joining'] = pd.to_datetime(data['Date of Joining'])


# ## Data Exploration
# 
# #### Descriptive Statistics

# In[13]:


print(data.describe())


# #### Grouping Data

# In[14]:


grouped_data = data.groupby(['Gender', 'Company Type'])['Mental Fatigue Score'].mean()
print(grouped_data)


# #### Frequency Counts

# In[15]:


gender_counts = data['Gender'].value_counts()
company_counts = data['Company Type'].value_counts()
print(gender_counts)
print(company_counts)


# ## Data Visualization
# 
# #### Plotting Distributions
# 
# ##### Histograms for Continuous Variables:

# In[16]:


import matplotlib.pyplot as plt

plt.hist(data['Mental Fatigue Score'], bins=20)
plt.title('Distribution of Mental Fatigue Scores')
plt.xlabel('Mental Fatigue Score')
plt.ylabel('Frequency')
plt.show()


# ##### Bar Charts for Categorical Variables:

# In[17]:


data['Company Type'].value_counts().plot(kind='bar')
plt.title('Employee Count by Company Type')
plt.xlabel('Company Type')
plt.ylabel('Number of Employees')
plt.show()


# #### Box Plots for Outlier Detection

# In[18]:


import seaborn as sns

sns.boxplot(x='Company Type', y='Mental Fatigue Score', data=data)
plt.title('Mental Fatigue Score by Company Type')
plt.show()


# ## Statistical Analysis
# 
# #### Correlation Analysis

# In[19]:


correlation_matrix = data.corr()
sns.heatmap(correlation_matrix, annot=True)
plt.title('Correlation Matrix')
plt.show()


# #### Hypothesis Testing

# In[20]:


from scipy import stats

male_scores = data[data['Gender'] == 'Male']['Mental Fatigue Score']
female_scores = data[data['Gender'] == 'Female']['Mental Fatigue Score']

t_stat, p_value = stats.ttest_ind(male_scores, female_scores)
print(f'T-statistic: {t_stat}, P-value: {p_value}')


# ##### Since the P-value is extremely small (much less than 0.05), we reject the null hypothesis. This means:
# There is a statistically significant difference in the average Mental Fatigue Scores between male and female employees. The high T-statistic and very small P-value indicate that the difference between the two groups is not due to random chance.
