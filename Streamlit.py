import pickle
import streamlit as st
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

model = pickle.load(open('model_cement_strength_prediction.pkl', 'rb'))

st.title('Cement Strength Prediction')
st.text('It takes 8 inputs: \n 1. cement\n 2. slag\n 3. ash\n 4. water\n 5. superplastic\n 6. coarseagg\n 7. fineagg\n 8. age')
st.text('It uses Machine Learning Algorithm to predict the strength of cement.')
st.header("Please enter the values below:")

a=st.number_input('cement', 0.0)
b=st.number_input('slag', 0.0)
c=st.number_input('ash', 0.0)
d=st.number_input('water', 0.0)
e=st.number_input('superplastic', 0.0)
f=st.number_input('coarseagg', 0.0)
g=st.number_input('fineagg', 0.0)
h=st.number_input('age', 0.0)

input_data = np.array([[a,b,c,d,e,f,g,h]])
input_data = pd.DataFrame(input_data, columns=['cement','slag','ash','water','superplastic','coarseagg','fineagg','age'])

if st.button("Calculate Strength", key="predict"):
    output = model.predict(input_data)
    st.success("Strength of cement : " + str(output[0]))

