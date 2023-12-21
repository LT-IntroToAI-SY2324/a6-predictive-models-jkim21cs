# Part 4 - Classification Writeup

After completing `a6_part4.py` answer the following questions

## Questions to answer

1. Comment out the StandardScaler and re-run your test. How accurate is the model? Why is that?
    The model is not as accurate without the StandardScaler b/c the StandardScaler helped to "normalize" the data making it easier for the algorithm to learn and predict the data. Without it, there are many outliers that may skew predictions. 

2. How accurate is the model with the StandardScaler? Is this model accurate enough for the given use case? Explain.
    The model with the StandardScaler is pretty accurate suggested by its prediction "correctness" from the testing set was 82%. I think the model is accurate enough for the given use case as it is looking at a "mean" for each variable and determining an answer. There may be outliers(ie. a teenage millionaire, or a very wealthy elder) but for general predictions this model does the job. 

3. Looking at the predicted and actual results, how did the model do? Was there a pattern to the inputs that the model was incorrect about?
    The model was pretty good. There was a pattern where for every one female their were 4 male predictions but it was difficult to see patterns in incorrect predictions to whether an individual purchased a car or not. 

4. Would a 34 year old Female who makes 56000 a year buy an SUV according to the model? Remember to scale the data before running it through the model.
    A 34 year old female who makes 56000 a year would not buy an SUV according to the model. 

