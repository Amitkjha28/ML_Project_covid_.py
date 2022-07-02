#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
from tkinter.ttk import Combobox


# In[2]:


import pickle
import joblib


# In[3]:


mymodel2=joblib.load('Joblib/rfc_model.jbl')


# In[4]:


class myclass:
    def __init__(self):
        self.window = Tk()
        self.window.title("Cvid App")
        self.window.geometry("%dx%d+%d+%d"%(900,680,150,30))
        
        self.headlbl = Label(self.window, text="Predict Covid ",font=("Algerian",50,'bold'))
        
        self.l1 = Label(self.window, text="Age")
        self.l2 = Label(self.window, text="Sex")
        self.l3 = Label(self.window, text="Patient Type ")
        self.l4 = Label(self.window, text="Intubed")
        self.l5 = Label(self.window, text="Pneumonia")
        self.l6 = Label(self.window, text="Pregnancy")
        self.l7 = Label(self.window, text="Diabetes")
        self.l8 = Label(self.window, text="Copd")
        self.l9 = Label(self.window, text="Asthma")
        self.l10 = Label(self.window, text="Inmsupr")
        self.l11 = Label(self.window, text="Hypertension")
        self.l12 = Label(self.window, text="Cardiovascular")
        self.l13 = Label(self.window, text="Obesity")
        self.l14 = Label(self.window, text="Renal_chronic")
        self.l15 = Label(self.window, text="Tobacco")
        self.l16 = Label(self.window, text="Contact_other_covid")
        self.l17 = Label(self.window, text="ICU")
        self.l18 = Label(self.window, text="Other Disease")
        self.l19 = Label(self.window, text="")
        
        self.l20 = Label(self.window, text="")
        self.l21 = Label(self.window, text="")
        
        
        self.list1 = ["No","Yes"]     
        
        self.t1 = Entry(self.window)
        
        self.v1 = StringVar()
        self.c1 = Combobox(self.window, values=["Female","Male"], textvariable=self.v1,state='readonly')
        self.v1.set("Female")
        self.c1.bind("<<ComboboxSelected>>",lambda e:self.checkGender())
        
        self.v2 = StringVar() 
        self.c2 = Combobox(self.window, values=["Hospitalized","Not Hospitalized"], textvariable=self.v2,state='readonly')
        self.v2.set("Hospitalized")
        self.c2.bind("<<ComboboxSelected>>",lambda e:self.checkICU())
        self.c2.bind("<<ComboboxSelected>>",lambda e:self.check_Intubed(),add=True)
        
        self.v3 = StringVar()
        self.c3 = Combobox(self.window, values=self.list1, textvariable=self.v3,state='readonly')
        self.check_Intubed()
        
        self.v4 = StringVar()
        self.c4 = Combobox(self.window,values=self.list1, textvariable=self.v4,state='readonly')
        self.v4.set("No")
        
        self.v5 = StringVar()
        self.c5 = Combobox(self.window, values=self.list1, textvariable=self.v5,state='disable')
        self.checkGender()
        self.v5.set("No")
        
        self.v6 = StringVar()
        self.c6 = Combobox(self.window,values=self.list1, textvariable=self.v6,state='readonly')
        self.v6.set("No")
        self.v7 = StringVar()
        self.c7 = Combobox(self.window,values=self.list1, textvariable=self.v7,state='readonly')
        self.v7.set("No")
        self.v8 = StringVar()
        self.c8 = Combobox(self.window,values=self.list1, textvariable=self.v8,state='readonly')
        self.v8.set("No")
        self.v9 = StringVar()
        self.c9 = Combobox(self.window,values=self.list1, textvariable=self.v9,state='readonly')
        self.v9.set("No")
        self.v10 = StringVar()
        self.c10 = Combobox(self.window,values=self.list1, textvariable=self.v10,state='readonly')
        self.v10.set("No")
        
        self.v11 = StringVar()
        self.c11 = Combobox(self.window,values=self.list1, textvariable=self.v11,state='readonly')
        self.v11.set("No")
        self.v12 = StringVar()
        self.c12 = Combobox(self.window,values=self.list1, textvariable=self.v12,state='readonly')
        self.v12.set("No")
        self.v13 = StringVar()
        self.c13 = Combobox(self.window,values=self.list1, textvariable=self.v13,state='readonly')
        self.v13.set("No")
        self.v14 = StringVar() 
        self.c14 = Combobox(self.window,values=self.list1, textvariable=self.v14,state='readonly')
        self.v14.set("No")
        
        self.v15 = StringVar()
        self.c15 = Combobox(self.window,values=self.list1, textvariable=self.v15,state='readonly')
        self.v15.set("No")
        self.v16 = StringVar()
        self.c16 = Combobox(self.window,values=self.list1, textvariable=self.v16)
        self.checkICU()
        
        self.v17 = StringVar()
        self.c17 = Combobox(self.window,values=self.list1, textvariable=self.v17,state='readonly')
        self.v17.set("No")
        
        self.b1 = Button(self.window, text="Predict",command=self.predict)
#         self.window.bind("<Return>",self.predict)

        # ******** PLacing *************
        self.headlbl.place(x=200, y=10)
        x1 = 40
        y1 = 130
        self.l1.place(x=x1, y=y1)
        self.t1.place(x=x1 + 150, y=y1)
        y1 += 50
        self.l2.place(x=x1, y=y1)
        self.c1.place(x=x1 + 150, y=y1)
        y1 += 50
        self.l3.place(x=x1, y=y1)
        self.c2.place(x=x1 + 150, y=y1)
        y1 += 50
        self.l4.place(x=x1, y=y1)
        self.c3.place(x=x1 + 150, y=y1)
        y1 += 50
        self.l5.place(x=x1, y=y1)
        self.c4.place(x=x1 + 150, y=y1)
        y1 += 50
        self.l6.place(x=x1, y=y1)
        self.c5.place(x=x1 + 150, y=y1)
        y1 += 50
        self.l7.place(x=x1, y=y1)
        self.c6.place(x=x1 + 150, y=y1)
        y1 += 50
        self.l8.place(x=x1, y=y1)
        self.c7.place(x=x1 + 150, y=y1)
        y1 += 50
        self.l9.place(x=x1, y=y1)
        self.c8.place(x=x1 + 150, y=y1)
        y1 += 50
        self.l10.place(x=x1, y=y1)
        self.c9.place(x=x1 + 150, y=y1)
        
        y2 = 130 
        x2 = 500
        self.l11.place(x=x2, y=y2)
        self.c10.place(x=x2 + 150, y=y2)
        y2 += 50
        self.l12.place(x=x2, y=y2)
        self.c11.place(x=x2 + 150, y=y2)
        y2 += 50
        self.l13.place(x=x2, y=y2)
        self.c12.place(x=x2 + 150, y=y2)
        y2 += 50
        self.l14.place(x=x2, y=y2)
        self.c13.place(x=x2 + 150, y=y2)
        y2 += 50
        self.l15.place(x=x2, y=y2)
        self.c14.place(x=x2 + 150, y=y2)
        y2 += 50
        self.l16.place(x=x2, y=y2)
        self.c15.place(x=x2 + 150, y=y2)
        y2 += 50
        self.l17.place(x=x2, y=y2)
        self.c16.place(x=x2 + 150, y=y2)
        y2 += 50
        self.l18.place(x=x2, y=y2)
        self.c17.place(x=x2 + 150, y=y2)
        y2 += 50     
        
        self.b1.place(x=x2+150, y=y2)

        y2 += 50
        self.l19.place(x=x2, y=y2)
        self.l20.place(x=x2, y=y2+30)
        self.l21.place(x=x2, y=y2+60)
  
        self.window.mainloop()
        
    def checkICU(self):
        if self.v2.get()=="Not Hospitalized" :
            self.c16.set("Does not apply")
            self.c16["state"]="disabled"
        else:
            self.c16.current(0)
            self.c16["state"]="readonly"
            
    def check_Intubed(self):
        if self.v2.get()=="Not Hospitalized" :
            self.c3.set("Does not apply")
            self.c3["state"]="disabled"
        else:
            self.c3.current(0)
            self.c3["state"]="readonly"
            
            
    def checkGender(self):
        if self.v1.get()=="Male" :
            self.c5.set("Does not apply")
            self.c5["state"]="disabled"
        else:
            self.c5.current(0)
            self.c5["state"]="readonly"
            
    def predict(self):
        age = int(self.t1.get()) 

        sex=(self.v1.get())
        if(sex=="Female"):
            sex=1
        else:
            sex=2 
            
        patient_type=(self.v2.get())
        if(patient_type=="Not Hospitalized"):
            patient_type=1
        else:
            patient_type=2
            
        intubed=self.v3.get()    
        if(intubed=='Yes'):
            intubed=1
        elif(intubed=='No'):
            intubed=2
        else:
            intubed=3
            
        pneumonia=self.v4.get()
        if(pneumonia=='Yes'):
            pneumonia=1
        else:
            pneumonia=2        
        
        pregnancy=self.v5.get()
        if(pregnancy=='Yes'):
            pregnancy=1
        elif(pregnancy=='No'):
            pregnancy=2
        else:
            pregnancy=3
            
        diabetes=self.v6.get()
        if(diabetes=='Yes'):
            diabetes=1
        elif(diabetes=='No'):
            diabetes=2
        else:
            diabetes=98
            
        copd=self.v7.get()
        if(copd=='Yes'):
            copd=1
        else:
            copd=2
            
        asthma=self.v8.get()
        if(asthma=='Yes'):
            asthma=1
        else:
            asthma=2
            
        inmsupr=self.v9.get()
        if(inmsupr=='Yes'):
            inmsupr=1
        else:
            inmsupr=2
            
        hypertension=self.v10.get()
        if(hypertension=='Yes'):
            hypertension=1
        else:
            hypertension=2
            
        cardiovascular=self.v11.get()
        if(cardiovascular=='Yes'):
            cardiovascular=1
        else:
            cardiovascular=2
            
        obesity=self.v12.get()
        if(obesity=='Yes'):
            obesity=1
        else:
            obesity=2
            
        renal_chronic=self.v13.get()
        if(renal_chronic=='Yes'):
            renal_chronic=1
        else:
            renal_chronic=2
        
        tobacco=self.v14.get()
        if(tobacco=='Yes'):
            tobacco=1
        else:
            tobacco=2
            
        contact_other_covid=self.v15.get()
        if(contact_other_covid=='Yes'):
            contact_other_covid=1
        else:
            contact_other_covid=2
            
        icu=self.v16.get()
        if(icu=='Yes'):
            icu=1
        else:
            icu=3
            
        other_disease=self.v17.get()
        if(other_disease=='Yes'):
            other_disease=1
        else:
            other_disease=2
        print(" Age : {}\n Sex : {}\n patient_type :{}\n intubed :{}\n pneumonia : {}\n pregnancy : {}\n diabetes : {}\n copd : {}\n asthma : {}\n inmsupr : {}\n hypertension : {}\n other_disease : {}\n cardiovascular : {}\n obesity : {}\n renal_chronic : {}\n tobacco : {}\n contact_other_covid : {}\n icu : {}\n".format( age,sex,patient_type,intubed,pneumonia,pregnancy,diabetes,copd,asthma,inmsupr,hypertension,other_disease,cardiovascular,obesity,renal_chronic,tobacco,contact_other_covid,icu))
        
    
        Prediction=mymodel2.predict_proba([[age,sex,patient_type,intubed,pneumonia,pregnancy,diabetes,copd,asthma,inmsupr,hypertension,
                                   other_disease,cardiovascular,obesity,renal_chronic,tobacco,contact_other_covid,icu]])
        print("Prediction : ",Prediction)
        output=round(Prediction[[0]][0][0]*100,2)
        
        self.l19.config(text="There is a {}% chance of  you getting Covid Positive (+ve)".format(output))
        self.l20.config(text="Stay Safe")
        self.l21.config(text="Thank You")
        
        


# In[5]:


obj=myclass()


# In[ ]:




