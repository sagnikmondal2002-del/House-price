import streamlit as st
import numpy as np 
import joblib
import warnings
warnings.filterwarnings('ignore')

#Uploading the model
model=joblib.load("random_search.pkl")

#Uploading the pickle file
st.title("House Price Prdeiction")
st.markdown("---")

bedroom=st.number_input(" number of bedroom",min_value=0,value=0)
bathroom= st.number_input(" number of bathroom",min_value=0,value=0)
living_area=st.number_input(" living area",min_value=0,value=2000)
condition_of_house=st.number_input( "condition of house",min_value=1,value=1)
school=st.number_input(" number of school",min_value=0,value=0)
x=[[bedroom,bathroom,living_area,condition_of_house,school]]
pred= st.button("Predict")
if pred==True:
    arr=np.array(x)
    price=int(model.predict(arr)[0])
    st.write(f"The price of the house is {price}")
else:
    st.write("Please click on the button")
