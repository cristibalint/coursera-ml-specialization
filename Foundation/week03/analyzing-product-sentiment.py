
# coding: utf-8

# # Predicting sentiment from product reviews
# 
# ## Fire up GraphLab Create

# In[1]:

import graphlab


# # Read some product review data
# 
# Loading reviews for a set of baby products. 

# In[2]:

products = graphlab.SFrame('amazon_baby.gl/')


# # Let's explore this data together
# 
# Data includes the product name, the review text and the rating of the review. 

# In[4]:

products.head()


# # Build the word count vector for each review

# In[3]:

products['word_count'] = graphlab.text_analytics.count_words(products['review'])


# In[4]:

products.head()


# In[5]:

graphlab.canvas.set_target('ipynb')


# In[6]:

products['name'].show()


# # Examining the reviews for most-sold product:  'Vulli Sophie the Giraffe Teether'

# In[7]:

giraffe_reviews = products[products['name'] == 'Vulli Sophie the Giraffe Teether']


# In[8]:

len(giraffe_reviews)


# In[9]:

giraffe_reviews['rating'].show(view='Categorical')


# # Build a sentiment classifier

# In[10]:

products['rating'].show(view='Categorical')


# # #Define what's a positive and a negative sentiment
# 
# We will ignore all reviews with rating = 3, since they tend to have a neutral sentiment.  Reviews with a rating of 4 or higher will be considered positive, while the ones with rating of 2 or lower will have a negative sentiment.   

# In[11]:

#ignore all 3* reviews
products = products[products['rating'] != 3]


# In[12]:

#positive sentiment = 4* or 5* reviews
products['sentiment'] = products['rating'] >=4


# In[13]:

products.head()


# ## Let's train the sentiment classifier

# In[14]:

train_data,test_data = products.random_split(.8, seed=0)


# In[16]:

sentiment_model = graphlab.logistic_classifier.create(train_data,
                                                     target='sentiment',
                                                     features=['word_count'],
                                                     validation_set=test_data,
                                                     max_iterations=15)


# # Evaluate the sentiment model

# In[17]:

sentiment_model.evaluate(test_data, metric='roc_curve')


# In[18]:

sentiment_model.show(view='Evaluation')


# # Applying the learned model to understand sentiment for Giraffe

# In[19]:

giraffe_reviews['predicted_sentiment'] = sentiment_model.predict(giraffe_reviews, output_type='probability')


# In[20]:

giraffe_reviews.head()


# ## Sort the reviews based on the predicted sentiment and explore

# In[21]:

giraffe_reviews = giraffe_reviews.sort('predicted_sentiment', ascending=False)


# In[22]:

giraffe_reviews.head()


# ## Most positive reviews for the giraffe

# In[23]:

giraffe_reviews[0]['review']


# In[24]:

giraffe_reviews[1]['review']


# ## Show most negative reviews for giraffe

# In[25]:

giraffe_reviews[-1]['review']


# In[26]:

giraffe_reviews[-2]['review']


# In[ ]:


