# Twitter-CSAM-Machine-Learning-Detector

LIBRARIES AND PROGRAM

I will be utilizing the Jupyter Notebook for my code.
Scikit-learn
NLTK
Pandas


DATA PREPARATION

Before the content of the tweets can be analyzed, we need to acquire them and convert them into a form that can be fed into our feature engineering program. 
Tweet Scraping. Rudniy is attempting to conduct scraping with his own program, will update


As of this week (July 3rd), Twitter has implemented a temporary "view cap" on 

Conversion of Tweets in .JSON format
.JSON can be easily imported into Jupyter Notebook
Pandas Dataframe: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html 

Tweet tokenizatation
Tokenized tweets refer to the process of breaking down a tweet into individual tokens or words. Tokenization is a fundamental step in natural language processing (NLP), where the goal is to convert raw text data into a format suitable for analysis and modeling.

I will use the Natural Language Toolkit (NLTK) to provide tokenizatiation functions

Tweet Tokenization



FEATURE ENGINEERING

Convert the Tweet text data into numerical features using appropriate text vectorization techniques, such as Bag-of-Words (BoW), Term Frequency-Inverse Document Frequency (TF-IDF), or word embeddings. Both SVM and Naive Bayes classifiers can work with these types of representations. 

Import .csv or .json into Jupyter Notebook

Text Vectorization
Bag-of-Words (BoW)
a. Bag-of-Words is a simple text representation technique that converts text data into a matrix of word occurrences. Each row in the matrix represents a tweet, and each column represents a unique word from the entire corpus of tweets.

b. Use scikit-learn library
Term Frequency-Inverse Document Frequency (TF-IDF)
a. TF-IDF is another text representation technique that takes into account the importance of words based on their frequency in a particular tweet and across the entire corpus.

b. Use scikit-learn library
Word Embeddings
a. Word embeddings represent words as dense vector representations in a continuous vector space. We can use pre-trained word embeddings or train our own embeddings 

b. Libraries such as Word2Vec or FastText 


MODEL SELECTION

Train the SVM classifier on the training data and evaluate its performance on a validation set. Similarly, train the Naive Bayes classifier and evaluate its performance on the same validation set. Choose appropriate hyperparameters for each model based on the performance.


MODEL EVALUATION

Compare the performance of both classifiers using evaluation metrics like accuracy, precision, recall, F1-score, etc., on the validation set. I can also use techniques like cross-validation to get more reliable estimates of the models' performance.


FINAL MODEL SELECTION

After evaluating both models, select the one that performs better on the validation set. I will also consider creating an ensemble of both models if they complement each other's strengths.


TESTING PHASE

Once you have chosen the best-performing model, test it on a separate testing dataset to assess its generalization performance. This dataset should not be used during training or hyperparameter tuning to avoid any bias.



RESULT ANALYSIS


 Analyze and interpret the results obtained from both classifiers. Discuss the insights gained from the comparison, strengths, and weaknesses of each approach, and any patterns observed in misclassifications.
