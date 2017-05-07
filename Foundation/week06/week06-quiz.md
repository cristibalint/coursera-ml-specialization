## Deep Learning ##

### 1. Which of the following statements are true? (Check all that apply) ###

Linear classifiers are never useful, because they cannot represent XOR.

Linear classifiers are useful, because, with enough data, they can represent anything.

**Having good non-linear features can allow us to learn very accurate linear classifiers.**

none of the above

### 2. A simple linear classifier can represent which of the following functions? (Check all that apply) ###

Hint: If you are stuck, see https://www.coursera.org/learn/ml-foundations/module/nqC1t/discussions/AAIUurrtEeWGphLhfbPAyQ

**x1 OR x2 OR NOT x3**

**x1 AND x2 AND NOT x3**

x1 OR (x2 AND NOT x3)

none of the above

### 3. Which of the the following neural networks can represent the following function? Select all that apply. ###

(x1 AND x2) OR (NOT x1 AND NOT x2)

Hint: If you are stuck, see https://www.coursera.org/learn/ml-foundations/module/nqC1t/discussions/AAIUurrtEeWGphLhfbPAyQ

![Deep Neural Network](quiz/or.png "Deep Neural Network")

### 4. Which of the following statements is true? (Check all that apply) ###

**Features in computer vision act like local detectors.**

Deep learning has had impact in computer vision, because it’s used to combine all the different hand-created features that already exist.

**By learning non-linear features, neural networks have allowed us to automatically learn detectors for computer vision.**

none of the above

### 5. If you have lots of images of different types of plankton labeled with their species name, and lots of computational resources, what would you expect to perform better predictions: ###

**a deep neural network trained on this data.**

a simple classifier trained on this data, using deep features as input, which were trained using ImageNet data.

### 6. If you have a few images of different types of plankton labeled with their species name, what would you expect to perform better predictions: ###

a deep neural network trained on this data.

**a simple classifier trained on this data, using deep features as input, which were trained using ImageNet data.**

---

## Deep features for image retrieval ##

### 1. What’s the least common category in the training data? ###

**bird**

dog

cat

automobile

### 2. Of the images below, which is the nearest ‘cat’ labeled image in the training data to the the first image in the test data (image_test[0:1])? ###

<img src="quiz/cat1.png">
<img src="quiz/cat2.png">
<img src="quiz/cat3.png">
<img src="quiz/cat4.png">
<img src="quiz/cat5.png">
<kbd>
  <img src="quiz/cat6.png">
</kbd>

### 3. Of the images below, which is the nearest ‘dog’ labeled image in the training data to the the first image in the test data (image_test[0:1])? ###

<img src="quiz/dog1.png">
<img src="quiz/dog2.png">
<img src="quiz/dog3.png">
<kbd>
  <img src="quiz/dog4.png">
</kbd>
<img src="quiz/dog5.png">
<img src="quiz/dog6.png">

### 4. For the first image in the test data, in what range is the mean distance between this image and its 5 nearest neighbors that were labeled ‘cat’ in the training data? ###

33 to 35

**35 to 37**

37 to 39

39 to 41

Above 41

### 5. For the first image in the test data, in what range is the mean distance between this image and its 5 nearest neighbors that were labeled ‘dog’ in the training data? ###

33 to 35

35 to 37

**37 to 39**

39 to 41

Above 41

### 6. On average, is the first image in the test data closer to its 5 nearest neighbors in the ‘cat’ data or in the ‘dog’ data? ###

**cat**

dog

### 7. In what range is the accuracy of the 1-nearest neighbor classifier at classifying ‘dog’ images from the test set? ###

50 to 60

**60 to 70**

70 to 80

80 to 90

90 to 100

