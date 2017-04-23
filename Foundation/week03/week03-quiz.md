## Clasification ##

### 1. The simple threshold classifier for sentiment analysis described in the video ###

Must have pre-defined positive and negative attributes
Must either count attributes equally or pre-define weights on attributes

### 2. For a linear classifier classifying between “positive” and “negative” sentiment in a review x, Score(x) = 0 implies (check all that apply): ###

We are uncertain whether the review is “positive” or “negative”

### 3. For which of the following datasets would a linear classifier perform perfectly? ###

![Example of dataset for which a linear classifier would perform perfectly](quiz/linear.png "Data set for linear classifier")

### 4. True or false: High classification accuracy always indicates a good classifier. ###

False

### 5. rue or false: For a classifier classifying between 5 classes, there always exists a classifier with accuracy greater than 0.18. ###

True

### 6. True or false: A false negative is always worse than a false positive. ###

False

### 7. Which of the following statements are true? (Check all that apply) ###

Test error tends to decrease with more training data until a point, and then does not change (i.e., curve flattens out)

---

## Analyzing product sentiment ##

### 1. Out of the 11 words in selected_words, which one is most used in the reviews in the dataset? ###

great

### 2. Out of the 11 words in selected_words, which one is least used in the reviews in the dataset? ###

wow

### 3. Out of the 11 words in selected_words, which one got the most positive weight in the selected_words_model? ###

love

### 4. Out of the 11 words in selected_words, which one got the most negative weight in the selected_words_model? ###

terrible

### 5. Which of the following ranges contains the accuracy of the selected_words_model on the test_data? ###

0.841 to 0.871

### 6. Which of the following ranges contains the accuracy of the sentiment_model in the IPython Notebook from lecture on the test_data? ###

0.901 to 0.931

### 7. Which of the following ranges contains the accuracy of the majority class classifier, which simply predicts the majority class on the test_data? ###

0.843 to 0.871

### 8. How do you compare the different learned models with the baseline approach where we are just predicting the majority class? ###

The model learned using all words performed much better than the other two. The other two approaches performed about the same.

### 9. Which of the following ranges contains the ‘predicted_sentiment’ for the most positive review for ‘Baby Trend Diaper Champ’, according to the sentiment_model from the IPython Notebook from lecture? ###

0.9 to 1.0

### 10. Consider the most positive review for ‘Baby Trend Diaper Champ’ according to the sentiment_model from the IPython Notebook from lecture. Which of the following ranges contains the predicted_sentiment for this review, if we use the selected_words_model to analyze it? ###

0.7 to 0.8

### 11. Why is the value of the predicted_sentiment for the most positive review found using the sentiment_model much more positive than the value predicted using the selected_words_model? ###

None of the selected_words appeared in the text of this review.
