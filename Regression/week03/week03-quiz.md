## Assesing Performance ##

### 1. If the features of Model 1 are a strict subset of those in Model 2, the TRAINING error of the two models can never be the same. ###

True

**False**

### 2. If the features of Model 1 are a strict subset of those in Model 2, which model will USUALLY have lowest TRAINING error? ###

Model 1

**Model 2**

It's impossible to tell with only this information

### 3. If the features of Model 1 are a strict subset of those in Model 2. which model will USUALLY have lowest TEST error? ###

Model 1

Model 2

**It's impossible to tell with only this information**

### 4. If the features of Model 1 are a strict subset of those in Model 2, which model will USUALLY have lower BIAS? ###

Model 1

**Model 2**

It's impossible to tell with only this information

### 5. Which of the following plots of model complexity vs. RSS is most likely from TRAINING data (for a fixed data set)? ###
![Complexity vs. RSS](quiz/plot.png)



a

b

**c**

d

### 6. Which of the following plots of model complexity vs. RSS is most likely from TEST data (for a fixed data set)? ###
![Complexity vs. RSS](quiz/plot.png)

**a**

b

c

d

### 7. It is always optimal to add more features to a regression model. ###

True

**False**

### 8. A simple model with few parameters is most likely to suffer from: ###

**High Bias**

High Variance

### 9. A complex model with many parameters is most likely to suffer from:  ###

High Bias

**High Variance**

### 10. A model with many parameters that fits training data very well but does poorly on test data is considered to be ###

accurate

biased

**overfitted**

poorly estimated

### 11. A common process for selecting a parameter like the optimal polynomial degree is: ###

Bootstrapping

Model estimation

Multiple regression

Minimizing test error

**Minimizing validation error**

### 12. Selecting model complexity on test data (choose all that apply): ###

Allows you to avoid issues of overfitting to training data

**Provides an overly optimistic assessment of performance of the resulting model**

Is computationally inefficient

**Should never be done**

### 13. Which of the following statements is true (select all that apply): For a fixed model complexity, in the limit of an infinite amount of training data, ###

The noise goes to 0

Bias goes to 0

**Variance goes to 0**

Training error goes to 0

Generalization error goes to 0

---

## Exploring the bias-variance tradeoff ##

### 1. Is the sign (positive or negative) for power_15 the same in all four models? ###

Yes, it is the same in all four models

**No, it is not the same in all four models**

### 2. The plotted fitted lines all look the same in all four plots ###

True

**False**

### 3. Which degree (1, 2, …, 15) had the lowest RSS on Validation data? ###

6

### 4. What is the RSS on TEST data for the model with the degree selected from Validation data? (Make sure you got the correct degree from the previous question) ###

**Between 1.2e+14 and 1.3e+14**

Between 1.7e+14 and 1.8e+14

Between 3.4e+13 and 3.5e+13

Between 5.6e+15 and 5.7e+17

