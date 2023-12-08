import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

'''
**********CREATE THE MODEL**********
'''

data = pd.read_csv("part2-training-testing-data/blood_pressure_data.csv")
x = data["Age"].values
y = data["Blood Pressure"].values

# Create your training and testing datasets:
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size = .2)
print(f"x:{x}")
print(f"x:{y}")
print(f"xtrain:{x}")
print(f"ytrain:{y}")
print(f"xtest:{x}")
print(f"ytest:{y}")
# Use reshape to turn the x values into 2D arrays:
xtrain = xtrain.reshape(-1,1)

# Create the model
model = LinearRegression().fit(xtrain, ytrain)

# get the coef_, intercept_ valuesm and r^2 values
# use float() to turn the arrays into a single float value
coef = round(float(model.coef_), 2)
intercept = round(float(model.intercept_), 2)
r_squared = model.score(xtrain, ytrain)

# print out the linear equation and r^2 value
print("Model's Linear Equation: y=",coef, "x+", intercept)
print("R Squared value:", r_squared)

'''
**********TEST THE MODEL**********
'''
#reshape the xtest data into a 2D array
xtest = xtest.reshape(-1,1)

# get the predicted y values for the xtest values - returns an array of the results
predict = model.predict(xtest)
# round the value in the np array to 2 decimal places
predict = np.around(predict, 2)

# compare the actual and predicted values
print("\nTesting Linear Model with Testing Data:")
for index in range(len(xtest)):
    actual = ytest[index] # gets the actual y value from the ytest dataset
    predicted_y = predict[index] # gets the predicted y value from the predict variable
    x_coord = xtest[index] # gets the x value from the xtest dataset
    print("x value:", float(x_coord), "Predicted y value:", predicted_y, "Actual y value:", actual)


'''
**********CREATE A VISUAL OF THE RESULTS**********
'''

# sets the size of the graph
plt.figure(figsize=(5, 4))

# creates a scatter plot and labels the axes
plt.scatter(xtrain,ytrain, c="red", Label="Training Data" )
plt.scatter(xtest, ytest, c="blue", Label= "Testing Data")
plt.scatter(xtest, predict, c="purple", Label = "Predictions")

plt.xlabel("Age")
plt.ylabel("Blood Pressure")
plt.title("Blood Pressure vs Age")
plt.plot(x, coef*x + intercept, c="r", label="Line of Best Fit")

# show the plot
plt.legend()
plt.show()

