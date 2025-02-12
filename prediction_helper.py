import pandas as pd
import joblib

# Load the trained model and scaler
best_model = joblib.load("artifacts\\best_model.joblib")
scaler = joblib.load("artifacts\\scaler.joblib")

def categorize_age(age_input):

    if age_input < 25:
        return 'Young Adult'
    elif 25 <= age_input < 40:
        return 'Adult'
    elif 40 <= age_input < 60:
        return 'Middle-Aged'
    else:
        return 'Senior'

def preprocess_input(input_dict):
    # Define the expected columns and initialize the DataFrame with zeros
    expected_columns = [
        'sex', 'no_of_dependents', 'smoker', 'bloodpressure', 'diabetes',
        'regular_ex','age_rank', 'bmi', 'Disease_Alzheimer',
       'Disease_Arthritis', 'Disease_Cancer', 'Disease_Diabetes',
       'Disease_Epilepsy', 'Disease_EyeDisease', 'Disease_HeartDisease',
       'Disease_High BP', 'Disease_NoDisease', 'Disease_Obesity'
    ]
    

    df = pd.DataFrame(0, columns=expected_columns, index=[0])

    # Manually assign values for each input
    for key, value in input_dict.items():
        if key == 'Gender' and value == 'Female':
            df['sex'] = 1
        elif key == 'Medical history':
            # Assign disease values (this part will need to be improved based on your exact input format)
            disease_map = {
                'Alzheimer': 'Disease_Alzheimer',
                'Arthritis': 'Disease_Arthritis',
                'Cancer': 'Disease_Cancer',
                'Diabetes': 'Disease_Diabetes',
                'Epilepsy': 'Disease_Epilepsy',
                'Eye Disease': 'Disease_EyeDisease',
                'Heart Disease': 'Disease_HeartDisease',
                'High BP': 'Disease_High BP',
                'None': 'Disease_NoDisease'
            }
            if value in disease_map:
                df[disease_map[value]] = 1
        elif key == 'Smoking Status' and value == 'Regular':
            df['smoker'] = 1
        elif key == 'Diabetic' and value == 'Yes':
            df['diabetes'] = 1
        elif key == 'Number of Dependents':
            df['no_of_dependents'] = value
        elif key == 'BMI':
            df['bmi'] = value
        elif key == 'Blood Pressure':
            df['bloodpressure'] = value
        elif key == 'Age':  
            age_input = value
            age_category = categorize_age(age_input)

            age_mapping = {
                'Young Adult': 0,
                'Adult': 1,
                'Middle-Aged': 2,
                'Senior': 3
            }

            df['age_rank'] = age_mapping.get(age_category, 1)
            print('age_rankss',df['age_rank'])
    df['regular_ex']= 0


    # Ensure scaling happens on the right columns
    df = handle_scaling(df)

    return df

def handle_scaling(df):
    # Assuming 'scaler' and 'scaler_with_cols' have been set correctly
    scaler_object = scaler
    columns_to_scale = scaler['columns_to_scale']
    scaler_model = scaler['scaler']


    # Apply scaling
    df[columns_to_scale] = scaler_model.transform(df[columns_to_scale])

    return df

def predict(input_dict):
    # Process the input
    input_df = preprocess_input(input_dict)

    # Check shape of input data before passing to the model
    print("Shape of input data for prediction:", input_df.shape)

    # Predict using the trained model
    prediction = best_model.predict(input_df)

    # Return the prediction
    return int(prediction[0])




