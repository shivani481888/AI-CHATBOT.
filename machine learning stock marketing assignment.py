

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# This program predicts stock market prices using a simple linear regression model.

# Step 1: Load dataset
data = pd.read_csv('python file/programs/Tesla.csv')  # Removed extra space in the file path
print(data.head(5))  # Display the first 5 rows of the dataset

# Step 2: Features (X) and Target (y)
x = data['Open'].values.reshape(-1, 1)  
y = data['Close']

# Step 3: Model training
model = LinearRegression()
model.fit(x, y)

# Step 4: Prediction
predictions = model.predict(x)

# Step 5: Plotting
plt.scatter(x, y, color='green', label='Actual close Prices')
plt.plot(x, predictions, color='red', label='Predicted close Prices')
plt.xlabel('Opening Price')
plt.ylabel('Closing Price')
plt.title('Stock Price Prediction')
plt.legend()
plt.grid()
plt.show()
 