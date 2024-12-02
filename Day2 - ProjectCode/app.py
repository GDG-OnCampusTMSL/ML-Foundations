import pickle as pkl 
import numpy as np 
import streamlit as st 

st.title("CO2 Emissions Prediction ")

with open ('model.pkl' , "rb" ) as file:
    model = pkl.load(file)

make = st.number_input("Make (Encoded)", min_value=0, step=1)
model_val = st.number_input("Model (Encoded)", min_value=0, step=1)
vehicle_class = st.number_input("Vehicle Class (Encoded)", min_value=0, step=1)
engine_size = st.number_input("Engine Size (L)", min_value=0.0, step=0.1)
cylinders = st.number_input("Cylinders", min_value=1, step=1)
transmission = st.number_input("Transmission (Encoded)", min_value=0, step=1)
fuel_type = st.number_input("Fuel Type (Encoded)", min_value=0, step=1)
fuel_consumption_city = st.number_input("Fuel Consumption City (L/100 km)", min_value=0.0, step=0.1)
fuel_consumption_hwy = st.number_input("Fuel Consumption Highway (L/100 km)", min_value=0.0, step=0.1)
fuel_consumption_comb = st.number_input("Fuel Consumption Combined (L/100 km)", min_value=0.0, step=0.1)
fuel_consumption_comb_mpg = st.number_input("Fuel Consumption Combined (mpg)", min_value=0.0, step=0.1)

if st.button("Predict CO2 Emissions") :
    input_features = np.array([make , model_val , vehicle_class , engine_size , cylinders ,transmission ,fuel_type, fuel_consumption_city , fuel_consumption_hwy  ,fuel_consumption_comb , fuel_consumption_comb_mpg]).reshape(1,-1)
    prediction = model.predict(input_features)
    st.write("Predicted CO2 EMISSIONS(G/KM) IS :" , prediction[0])
    