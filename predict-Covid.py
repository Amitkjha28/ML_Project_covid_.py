#!/usr/bin/env python
# coding: utf-8

# ## Note:
# 
#     1 - Yes 
#     2 - No 
#     97 - Does Not Apply 
#     98 - It is Ignored 
#     99 - No Specified
#     
#     Sex : 1 - Female , 2 - Male
#     
#     Patient_type :  1 - Not Hospitalized , 2 - Hosptalized
#     
#     intubed : 1 - Patient used Ventilator (Yes) and “2” - Patient did not used Ventilator (No)
#     
#     covid_res : 1 - covid Positive (+ve) , 2  Negative (-ve) , 3 - Awaiting Process  

# In[1]:


import pandas as pd


# In[ ]:





# In[2]:


df=pd.read_csv('covid.csv')


# In[3]:


df.head(2)


# In[4]:


df.columns


# In[5]:


covid_data=df.drop(['id', 'entry_date', 'date_symptoms', 'date_died'],axis=1)


# In[6]:


covid_data.head()


# In[7]:


covid_data.describe()


# In[8]:


covid_data.isnull().sum()


# In[9]:


for i in covid_data.columns:
    print("Unique value in {} :".format(i),covid_data[i].unique())
    


# In[10]:


for i in covid_data.columns:
    print(covid_data[i].value_counts())
    print("********************************")


# In[11]:


mydf = ['sex','patient_type','intubed','pneumonia','pregnancy','diabetes','copd','asthma','inmsupr','hypertension',
        'other_disease','cardiovascular','obesity','renal_chronic','tobacco','contact_other_covid','covid_res','icu']
for i in mydf:
    covid_data=covid_data[covid_data[i]<98]
    covid_data[i].replace({97:3},inplace=True)
covid_data


# In[12]:


covid_data=covid_data[covid_data['covid_res']!=3]
covid_data


# In[13]:


for i in covid_data.columns:
    print(covid_data[i].value_counts())
    print("********************************")


# In[14]:


covid_data.corr()


# In[15]:


import seaborn as sns
import matplotlib.pylab as plt


# In[16]:


plt.figure(figsize=(20,20))
sns.heatmap(covid_data.corr(),annot=True,cmap='winter',vmin=0,vmax=1)
plt.show()


# In[17]:


sns.pairplot(covid_data.corr())
plt.show()


# In[ ]:





# In[18]:


x=covid_data.drop(['covid_res'],axis=1)
y=covid_data['covid_res']


# In[19]:


x


# In[20]:


y


# In[ ]:





# In[21]:


from sklearn.ensemble import ExtraTreesClassifier


# In[22]:


model = ExtraTreesClassifier()


# In[23]:


model.fit(x,y)


# In[24]:


print(model.feature_importances_)


# In[25]:


feat_importances = pd.Series(model.feature_importances_, index=x.columns)
feat_importances.nlargest(18).plot(kind='barh')
plt.show()


# In[26]:


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)


# In[27]:


print(" Shape of X_train is:{}\n Shape of Y_train is:{}\n Shape of X_test is:{}\n Shape of Y_test is:{}\n".format(x_train.shape,y_train.shape,x_test.shape,y_test.shape))


# In[ ]:





# In[28]:


# RandomForestClassifier


# In[29]:


from sklearn import metrics


# In[30]:


from sklearn.ensemble import RandomForestClassifier


# In[31]:


rf_classifier=RandomForestClassifier()


# In[32]:


rf_classifier.fit(x_train,y_train)


# In[33]:


pre_rfc=rf_classifier.predict(x_test)


# In[34]:


rfc_score = metrics.accuracy_score(y_test, pre_rfc)


# In[35]:


print(rfc_score)


# In[36]:


rfc_prob=rf_classifier.predict_proba(x_test)[[0]][0]
rfc_prob


# In[ ]:





# In[37]:


#DecisionTreeClassifier


# In[38]:


from sklearn.tree import DecisionTreeClassifier


# In[39]:


DTree = DecisionTreeClassifier(max_depth =10)


# In[40]:


DTree.fit(x_train,y_train)


# In[41]:


predTree = DTree.predict(x_test)


# In[42]:


decisionTree_score=metrics.accuracy_score(y_test, predTree)
decisionTree_score


# In[43]:


decisionTree_prob=DTree.predict_proba(x_test)[[0]][0]
decisionTree_prob


# In[ ]:





# In[44]:


import pickle
import joblib 


# In[45]:


# DecisionTreeClassifier Save model  


# In[46]:



file = open('Pickle/DTree_model.pkl', 'wb')
pickle.dump(DTree, file)


# In[47]:


joblib.dump(DTree,'Joblib/DTree_model.jbl')


# In[48]:


# RandomForestClassifier Save model 


# In[ ]:


pickle.dump(rf_classifier,open('Pickle/rfc_model.pkl', 'wb'))  


# In[ ]:


joblib.dump(rf_classifier,'Joblib/rfc_model.jbl')


# In[ ]:




