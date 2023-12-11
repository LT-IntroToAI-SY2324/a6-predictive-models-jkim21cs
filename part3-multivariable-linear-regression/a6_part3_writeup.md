# Part 3 - Multivariable Linear Regression Writeup

After completing `a6_part3.py` answer the following questions

## Questions to answer

1. What is the R Squared coefficient for your model? What does that mean about the model in relation to your data?
    The R squared coefficient is 0.86. This value denotes that there is a "high" correlation between the number miles and age of a car.

2. Is your model accurate? Why or why not?
    The model is pretty accurate, the predicted and actual values are within a  range of one another sometimes giving predictions that are only 40 dollars off but others 2000. 

3. What does the model predict a 10-year-old car with 89000 miles is worth? What about a car that is 20 years old with 150000 miles? 
    The model predicts that a 10 year-old car with 89000 costs $7795.70. A car that is 20 years old with 150000 miles is worth -$118.14.

4. You may notice that some of your predicted results are negative. This is occurring when the value of age and the mileage of the car are very high. Why do you think this is happening?
    This may be happening because as a car grows older and the mileage increases, the value of the car begins to decrease. So the loss of value is indicated by negative predictions. 