import pickle
import numpy as np

# Load the models and data (adapt to your actual file paths if necessary)
pipe = pickle.load(open('pipe.pkl', 'rb'))
x = pickle.load(open('x.pkl', 'rb'))

# Example input values (modify as needed for your test case)
Company = 'Dell'  # Example brand
Type = 'Ultrabook'  # Example type
ram = 16  # Example RAM
Weight = 1.8  # Example weight in kg
Touchscreen = 'Yes'  # Example touchscreen option
ips = 'Yes'  # Example IPS option
screen_size = 15.6  # Example screen size
resolution = '1920x1080'  # Example screen resolution
Cpu = 'Intel Core i7'  # Example CPU brand
hdd = 1024  # Example HDD size in GB
ssd = 512  # Example SSD size in GB
Gpu = 'NVIDIA'  # Example GPU brand
os = 'Windows'  # Example OS

# Convert inputs
PixPInch = None
if Touchscreen == 'Yes':
    Touchscreen = 1
else:
    Touchscreen = 0

if ips == 'Yes':
    ips = 1
else:
    ips = 0

X_res = int(resolution.split('x')[0])
Y_res = int(resolution.split('x')[1])
PixPInch = ((X_res ** 2) + (Y_res ** 2)) ** 0.5 / screen_size

# Create query array
query = np.array([Company, Type, ram, Weight, Touchscreen, ips, PixPInch, Cpu, hdd, ssd, Gpu, os])

# Reshape the query for prediction
query = query.reshape(1, 12)

# Print the query array and its dtype in PyCharm terminal
print("Query Array:", query)
print("Query dtype:", query.dtype)
