import streamlit as st
import pickle

# Load the trained model using pickle
with open('financial_inclusion_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Create input fields for features
st.title("Financial Inclusion Prediction")
feature1 = st.number_input("country")
feature2 = st.number_input("year")
feature3 = st.number_input("uniqueid")
feature4 = st.number_input("location_type")
feature5 = st.number_input("cellphone_access")
feature6 = st.number_input("household_size")
feature7 = st.number_input("age_of_respondent")
feature8 = st.number_input("gender_of_respondent")
feature9 = st.number_input("relationship_with_head")
feature10 = st.number_input("marital_status")
feature11 = st.number_input("education_level")
eature11 = st.number_input("job_type")
# Add more input fields as needed

# Predict button
if st.button("Predict"):
    input_data = [[feature1, feature2]]  # Adjust based on your features
    prediction = model.predict(input_data)
    st.write("Prediction:", prediction)