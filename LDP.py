import streamlit as st
import pandas as pd

from sklearn.tree import DecisionTreeClassifier

import xgboost as xgb

import plotly.express as px
import joblib

st.set_page_config(page_title="OAdarkwa Loans")

header=st.container()
dataset=st.container()
filt=st.container()
result=st.container()



with header:
    st.title("OAdarkwa Loan Pre-Approval")

st.write("Answer the following questions to get a pre-approval:")
    
t=st.selectbox("Choose Loan Term",options=["36 months","60 months"])
a=st.number_input("Loan Amount [$]",value=45000)
d=st.number_input("Estimated Total Debt [$]",value=20000)
ai=st.number_input("Estimated Gross Annual Income [$]",value=75000)
h=st.selectbox("Home Ownership [Primary Residence]",options=["Rent","Mortgage","Own"])
p=st.selectbox("Purpose of Loan",options=["Car","Debt Consolidation","small business"])




DTI=d/ai
RBTI=d/ai
RBTL=d/a


if t=="36 months":
    	x_t=0
else:
    	x_t=1

x_h=[0,0,0,0,1]
x_p=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]

if h=="Rent":
	x_h=[0,0,0,0,1]
elif h=="Own":
	x_h=[0,0,0,1,0]
else: x_h=[1,0,0,0,0]


if p=="Car":
	x_p=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]

elif p=="Debt Consolidation":
	x_p=[0,1,0,0,0,0,0,0,0,0,0,0,0,0]
else: x_p=[0,0,0,0,0,0,0,0,0,0,0,1,0,0]




z=pd.DataFrame()
z["term_ 60 months"]=[x_t]
z["LTI"]=[DTI]
z["RBTI"]=[RBTI]
z["RBTL"]=[RBTL]
#st.write(z)

hvd=pd.DataFrame({"home_ownership_MORTGAGE":[x_h[0]],"home_ownership_NONE":[x_h[1]],"home_ownership_OTHER":[x_h[2]],"home_ownership_OWN":[x_h[3]],"home_ownership_RENT":[x_h[4]]})

pvd=pd.DataFrame({"purpose_credit_card":[x_p[0]],"purpose_debt_consolidation":[x_p[1]],"purpose_educational":[x_p[2]],"purpose_home_improvement":[x_p[3]],"purpose_home_improvement":[x_p[4]],"purpose_house":[x_p[5]],"purpose_major_purchase":[x_p[6]],"purpose_medical":[x_p[7]],"purpose_moving":[x_p[8]],"purpose_other":[x_p[9]],"purpose_renewable_energy":[x_p[10]],"purpose_small_business":[x_p[11]],"purpose_vacation":[x_p[12]],"purpose_wedding":[x_p[13]]})


x=pd.concat([pvd,hvd,z],axis=1)

#st.write(x)

model=joblib.load('Loan_Def_Model-2')

p=model.predict(x)

if p[0]==0:
	st.write("Your loan application cannot be pre-approved now. Please contact the helpline for additional information")
else: st.write("Your loan application is pre-approved. Loan Services Department will reach out to you on your phone number on file for the next steps. Thank you!") 






