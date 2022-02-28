#!/usr/bin/env python
# coding: utf-8

# In[37]:


import pandas as pd


# In[38]:


raw_data = pd.read_csv("Absenteeism-data.csv")


# In[39]:


df = raw_data.copy()


# In[40]:


pd.options.display.max_columns=None
pd.options.display.max_rows=None


# In[41]:


df.info()


# In[42]:


df= df.drop(["ID"],axis=1)


# In[43]:


df["Reason for Absence" ].min()


# In[44]:


df["Reason for Absence" ].max()


# In[45]:


pd.unique(df["Reason for Absence"])


# In[61]:


reason_for_absence = pd.get_dummies(df["Reason for Absence"],drop_first=True)


# In[62]:


reason_for_absence


# In[63]:


reason_for_absence["check"] = reason_for_absence.sum(axis=1)


# In[64]:


reason_for_absence


# In[65]:


reason_for_absence["check"].sum()


# In[66]:


reason_for_absence["check"].unique()


# In[78]:


reason_for_absence= reason_for_absence.drop(["check"],axis=1)


# # Grouping the reason for absence

# In[79]:


df.columns.values


# In[80]:


reason_for_absence.columns.values


# In[107]:


df=df.drop(["Reason for Absence"],axis=1)


# In[108]:


df.info()


# In[109]:


reason_type1=reason_for_absence.iloc[:,1:14].max(axis=1)
reason_type2=reason_for_absence.iloc[:,15:17].max(axis=1)
reason_type3=reason_for_absence.iloc[:,18:21].max(axis=1)
reason_type4=reason_for_absence.iloc[:,22:28].max(axis=1)


# In[98]:


df=pd.concat([df,reason_type1,reason_type2,reason_type3,reason_type4],axis=1)


# In[102]:


df.columns.values


# In[103]:


columns=['Reason for Absence', 'Date', 'Transportation Expense',
       'Distance to Work', 'Age', 'Daily Work Load Average',
       'Body Mass Index', 'Education', 'Children', 'Pets',
       'Absenteeism Time in Hours', "Reason_1", "Reason_2", "Reason_3", "Reason_4"]


# In[104]:


df.columns = columns


# In[110]:


df.head()


# # Reordering the columns
# 

# In[112]:


df.columns


# In[113]:


columns = ['Reason_1', 'Reason_2', 'Reason_3',
       'Reason_4','Date', 'Transportation Expense', 'Distance to Work', 'Age',
       'Daily Work Load Average', 'Body Mass Index', 'Education', 'Children',
       'Pets', 'Absenteeism Time in Hours' ]


# In[115]:


df= df[columns]


# In[116]:


df.head()


# # creating the check point

# In[402]:


df_reason_mod= df.copy()


# In[403]:


df_reason_mod.head()


# # date column

# In[404]:


type(df_reason_mod["Date"][0])


# In[405]:


df_reason_mod["Date"] = pd.to_datetime(df_reason_mod["Date"] )


# In[406]:


df_reason_mod["Date"] = pd.to_datetime(df_reason_mod["Date"],format='%d%m%Y')


# In[407]:


df_reason_mod.info()


# # extract the month value

# In[408]:


df_reason_mod["Date"][0]


# In[409]:


df_reason_mod["Date"].dt.month


# In[410]:


df_reason_mod["Date"][0].month


# In[411]:


df_reason_mod.shape


# In[412]:


lists=[]


# In[413]:


for i in range(df_reason_mod.shape[0]):
    lists.append(df_reason_mod["Date"][i].month)


# In[414]:


len(lists)


# In[415]:


df_reason_mod["Month_value"] = lists


# In[416]:


df_reason_mod.head()


# # Day of the week

# In[417]:


df_reason_mod["Date"][0]


# In[418]:


df_reason_mod["Date"][0].day_of_week


# In[419]:


def day0ftheweek(day):
    return day.day_of_week


# In[420]:


df_reason_mod["Day of the week"]=df_reason_mod["Date"].apply(day0ftheweek)


# In[421]:


df_reason_mod.info()


# In[422]:


df_reason_mod.head()


# In[424]:


df_reason_mod = df_reason_mod.drop(["Date"], axis=1)


# In[426]:


df_reason_mod.head()


# In[427]:


df_reason_mod.columns.values


# In[428]:


df_columns_names = ['Reason_1', 'Reason_2', 'Reason_3', 'Reason_4', 'Month_value',
       'Day of the week','Transportation Expense', 'Distance to Work', 'Age',
       'Daily Work Load Average', 'Body Mass Index', 'Education',
       'Children', 'Pets', 'Absenteeism Time in Hours']


# In[429]:


df_reason_mod_1=df_reason_mod[df_columns_names]


# In[430]:


df_reason_mod_1.head()


# # education column into binary data

# In[431]:


df_reason_mod_1  = df_reason_mod_1.copy()


# In[434]:


df_reason_mod_1["Education"].unique()


# In[439]:


Edu = pd.get_dummies(df_reason_mod_1["Education"])


# In[451]:


Edu.sum(axis=0)


# In[453]:


Edu.value_counts()


# In[443]:


Edu["check"] = Edu.sum(axis=1)


# In[449]:


Edu["check"].sum()


# In[447]:


pd.unique(Edu["check"])


# In[450]:


Edu.drop("check",axis=1)


# In[465]:


df_reason_mod_1["Education"]  = df_reason_mod_1["Education"].map({1:0,2:1,3:1,4:1})


# In[466]:


df_reason_mod_1["Education"].unique()


# In[476]:


df_reason_mod_1 = df_reason_mod_1.drop("Eduacation",axis=1)


# In[477]:


df_reason_mod_1 = df_reason_mod_1.drop("check",axis=1)


# # final dataset

# In[478]:


df_cleaned = df_reason_mod_1.copy()


# In[479]:


df_cleaned


# In[ ]:




