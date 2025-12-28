import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# Training data
X = np.array([[5],[8], [13],[17],[21],])

y = np.array([31,59,78,91,110])

# Model
print("niteesh_pandey")
model = LinearRegression()
model.fit(X, y)

# Prediction
area = int(input("kripya batao"))
prediction = model.predict([[area]])

print("Predicted output:", prediction[0])
