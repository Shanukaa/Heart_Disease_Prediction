import streamlit as st
import numpy as np
import joblib

# Load the trained SVM model from the pickle file
svm_model = joblib.load('Heart_Disease.pkl')

# Function to predict heart disease
def predict_heart_disease(input_data):
    # Reshape the input data
    input_data_reshaped = np.asarray(input_data).reshape(1, -1)
    # Make prediction
    prediction = svm_model.predict(input_data_reshaped)
    return prediction[0]

def main():
    # Set title and description with styling
    st.markdown('<h1 style="color: lightblue;">Heart Disease Prediction</h1>', unsafe_allow_html=True)
    st.write('Enter Patient Details.')

    # Input fields
    age = st.slider('Age', 29, 77, 40)
    sex = st.selectbox('Sex', ['Male', 'Female'])
    cp = st.slider('Chest Pain Type', 0, 3, 1)
    trestbps = st.slider('Resting Blood Pressure', 94, 200, 120)
    chol = st.slider('Serum Cholesterol', 126, 564, 240)
    fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', ['False', 'True'])
    restecg = st.selectbox('Resting Electrocardiographic Results', ['Normal', 'ST-T wave abnormality', 'Probable or definite left ventricular hypertrophy'])
    thalach = st.slider('Maximum Heart Rate Achieved', 71, 202, 150)
    exang = st.selectbox('Exercise Induced Angina', ['No', 'Yes'])
    oldpeak = st.slider('ST Depression Induced by Exercise Relative to Rest', 0.0, 6.2, 3.0)
    slope = st.selectbox('Slope of the Peak Exercise ST Segment', ['Upsloping', 'Flat', 'Downsloping'])
    ca = st.slider('Number of Major Vessels Colored by Flourosopy', 0, 4, 2)
    thal = st.selectbox('Thalassemia', ['Normal', 'Fixed defect', 'Reversible defect'])

    # Map categorical inputs to numerical values
    sex = 0 if sex == 'Male' else 1
    fbs = 0 if fbs == 'False' else 1
    exang = 0 if exang == 'No' else 1
    if restecg == 'Normal':
        restecg = 0
    elif restecg == 'ST-T wave abnormality':
        restecg = 1
    else:
        restecg = 2
    if slope == 'Upsloping':
        slope = 0
    elif slope == 'Flat':
        slope = 1
    else:
        slope = 2
    if thal == 'Normal':
        thal = 1
    elif thal == 'Fixed defect':
        thal = 2
    else:
        thal = 3

    # Predict heart disease
    input_data = (age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)
    prediction = predict_heart_disease(input_data)

    # Style prediction result
    if prediction == 0:
        st.markdown('<p style="color: green; font-size: 20px; margin-top: 20px; text-align:center;">The Patient does not have a Heart Disease</p>', unsafe_allow_html=True)
    else:
        st.markdown('<p style="color: red; font-size: 20px; margin-top: 20px; text-align:center;">The Patient has Heart Disease</p>', unsafe_allow_html=True)

if __name__ == '__main__':
    main()
