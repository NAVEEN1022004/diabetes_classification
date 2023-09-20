# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 19:28:45 2023

@author: NAVEEN
"""
import numpy as np
import streamlit as st
 
import pickle 
dia_model = pickle.load(open('C:/models/dia_model.sav','rb'))

def dia_prediction(cholesterol,glucose,hdl_chol,age,gender,height,weight,systolic_bp,diastolic_bp,waist,hip):
  inp=np.array([[cholesterol,glucose,hdl_chol,age,gender,height,weight,systolic_bp,diastolic_bp,waist,hip]]).astype(np.float64)
  pred=dia_model.predict(inp)
  print(pred)
  return pred
  
  
  
def main():
  with st.container():     #title of web 
        st.title('diabetes_classification_web')
        st.title('check your health')
        #getting inputdata
        cholesterol=st.text_input('cholesterol')
        glucose=st.text_input('glucose')
        hdl_chol=st.text_input('hdl_chol')
        age=st.text_input('age')
        gender=st.text_input('gender')
        height=st.text_input('height')
        weight=st.text_input('weight')
        systolic_bp=st.text_input('systolic_bp')
        diastolic_bp=st.text_input('diastolic_bp')
        waist=st.text_input('waist')
        hip=st.text_input('hip')
       

        dia=""
   #creating a button
        if st.button("check your health "):
          dia=int(dia_prediction(cholesterol,glucose,hdl_chol,age,gender,height,weight,systolic_bp,diastolic_bp,waist,hip))
        print(dia)
        if(dia==0):
           dia='no diabetes'
        elif(dia==1):
           dia='you are affected by diabetes'
        st.success(dia)
     
          
if __name__=='__main__':
   main()