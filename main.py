
import streamlit as st
from prediction_helper import predict
valid_input = True  
# Define the page layout
st.header('Health Insurance Claim Amount Predictor')

categorical_options = {
    'Gender': ['Male', 'Female'],
    'Smoking Status': ['No Smoking', 'Regular'],
    'Diabetic':['Yes','No'],
    'Medical History': [
         'Alzheimer', 'Arthritis', 'Cancer',
       'Diabetes', 'Epilepsy', 'Eye Disease',
       'Heart Disease', 'High BP', 'None',
       'Obesity'
    ]
}

# Create four rows of three columns each
row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
#row4 = st.columns(3)

# Assign inputs to the grid
with row1[0]:
    age_input = st.number_input('Age', min_value=18, step=1, max_value=100)
with row1[1]:
    number_of_dependents = st.number_input('Number of Dependants', min_value=0, step=1, max_value=20)
with row1[2]:
    sex = st.selectbox('Gender', categorical_options['Gender'])

with row2[0]:
    smoker = st.selectbox('Smoking Status', categorical_options['Smoking Status'])
with row2[1]:
    bloodpressure = st.number_input('Blood Pressure', min_value=0, value = 60,step=1, max_value=200)
    if bloodpressure == 0:
        st.warning("Please enter a valid blood pressure value.")
        valid_input = False 
    elif bloodpressure < 50 or bloodpressure > 200:
        st.warning("Blood Pressure should be between 50 and 200!")
        valid_input = False 
with row2[2]:
    bmi = st.number_input('BMI', min_value=0,value = 15, step=1, max_value=100)
    if bmi == 0:
        st.warning("Please enter a valid BMI value.")
        valid_input = False 

with row3[0]:
    diabetes = st.selectbox('Diabetic', categorical_options['Diabetic'])
with row3[1]:
    diseases = st.selectbox('Medical History', categorical_options['Medical History'])




# with row3[2]:
#     bmi_category = st.selectbox('BMI Category', categorical_options['BMI Category'])

# with row4[0]:
#     smoking_status = st.selectbox('Smoking Status', categorical_options['Smoking Status'])
# with row4[1]:
#     region = st.selectbox('Region', categorical_options['Region'])
# with row4[2]:
#     medical_history = st.selectbox('Medical History', categorical_options['Medical History'])

# Create a dictionary for input values
input_dict = {
    'Age': age_input,
    'Number of Dependents': number_of_dependents,
    'Gender':sex,
    'Smoking Status': smoker,
    'Blood Pressure': bloodpressure,
    'BMI': bmi,
    'Diabetic': diabetes,
    'Medical history': diseases,
   

}

# Button to make prediction
if st.button('Predict'):
    if valid_input:
        prediction = predict(input_dict)
        st.success(f'Predicted Health Insurance Cost: {prediction}')
    else:
        st.error("Fix the errors above before proceeding.")
   

    

st.markdown("[Click here to read more about the project](https://rgkamakshi.github.io)")
