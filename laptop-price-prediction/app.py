import streamlit as st
import pickle
import numpy as np

pipe = pickle.load(open('pipe.pkl', 'rb'))
x = pickle.load(open('x.pkl', 'rb'))

st.title("Laptop Price Predictor")

# Removed the 'Company' input
Type = st.selectbox('Type', x['TypeName'].unique())
ram = st.selectbox('RAM (in GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64])
Weight = st.number_input('Weight of the laptop')
Touchscreen = st.selectbox('Touchscreen', ['Yes', 'No'])
ips = st.selectbox('IPS', ['Yes', 'No'])
screen_size = st.number_input('Screen Size(In Inches)')
resolution = st.selectbox('Screen Resolution', ['2560x1600', '1440x900', '1920x1080', '2880x1800', '1366x768',
                                                '2304x1440', '3200x1800', '1920x1200', '2256x1504', '3840x2160',
                                                '2160x1440', '2560x1440', '1600x900', '2736x1824', '2400x1600'])
Cpu = st.selectbox('CPU', x['Cpu brand'].unique())

hdd = st.selectbox('HDD(in GB)', [0, 128, 256, 500, 1024, 2048])
ssd = st.selectbox('SSD(in GB)', [0, 128, 256, 500, 1024])
Gpu = st.selectbox('GPU', x['Gpu_brand'].unique())
os = st.selectbox('OS', x['OS'].unique())

if st.button('Predict Price'):
    if Weight == 0 or screen_size == 0:
        st.warning("Please fill all fields before predicting.")
    else:
        PixPInch = None
        Touchscreen = 1 if Touchscreen == 'Yes' else 0
        ips = 1 if ips == 'Yes' else 0

        X_res = int(resolution.split('x')[0])
        Y_res = int(resolution.split('x')[1])
        PixPInch = ((X_res**2) + (Y_res**2))**0.5 / screen_size

        # Select a random brand (Company) for prediction
        random_brand = np.random.choice(x['Company'].unique())  # Randomly select a brand for output

        # Create the query array without 'Company'
        query = np.array([random_brand, Type, ram, Weight, Touchscreen, ips, PixPInch, Cpu, hdd, ssd, Gpu, os], dtype=object)
        query = query.reshape(1, 12)

        # Make prediction
        predicted_price = np.exp(pipe.predict(query)[0])

        # Display the randomly selected brand with the predicted price
        st.title(f"The predicted price of the {random_brand} laptop is ₹ {predicted_price:.2f}")
