# Machine learning introduction

Summary: This project is about introduction into machine learning and particularly about primary data analysis with some practical basics.

💡 [Tap here](https://new.oprosso.net/p/4cb31ec3f47a4596bc758ea1861fb624) **to leave your feedback on the project**. It's anonymous and will help our team make your educational experience better. We recommend completing the survey immediately after the project.

## Contents

1. [Chapter I. Preamble](#chapter-i-preamble)
2. [Chapter II. Introduction](#chapter-ii-introduction) \
    2.1. [Steps to build a model](#steps-to-build-a-model) \
    2.2. [ML algorithms](#ml-algorithms) \
        2.2.1. [Supervised learning](#supervised-learning) \
        2.2.2. [Unsupervised learning](#unsupervised-learning)
3. [Chapter III. Goal](#chapter-iii-goal) 
4. [Chapter IV. Instructions](#chapter-iv-instructions)
5. [Chapter V. Task](#chapter-v-task)


## Chapter I. Preamble

“With the ever-increasing amounts of data in electronic form, the need for automated methods for data analysis continues to grow. The goal of machine learning is to develop methods that can automatically detect patterns in data, and then to use the uncovered patterns to predict future data or other outcomes of interest” -  we start our course from definition of machine learning from one of widely known book - “Machine Learning A Probabilistic Perspective” by Kevin P. Murphy. 

There are a lot of problems that are solved with ML methods:
* The problem of housing price prediction. We are trying to define a cost of an object with set of features such as quality of repair, footage and area
* What disease does the patient have if we observe a certain set of symptoms?
* Will the client of the bank return the loan if his income is X and he has a good credit history?
* What products are suitable to show for users on the main page of the online store to speed up his/her successful search?

In most cases we can answer all these questions. But it is much better to have a machine that can do this work without prejudice and do it many times faster. Data calls for automated methods of analysis, which is what machine learning provides. We define machine learning as a set of methods that can automatically detect patterns in data, and then use the uncovered patterns to predict future data.

To sum up, this course will show you what Machine Learning is. After reading all the materials and practicing labs, you will master all the basic approaches of building models and learn how to predict the future.

## Chapter II. Introduction

### Steps to build a model

![day_1_scheme](misc/images/scheme.png)

Suppose you are a very clever house seller. You know everything about the real estate market 
(*data* and *features*) and understand how the price depends on various factors (*algorithm*). 
For example, you know that the more bedrooms an apartment has, the more expensive it is. 
But how can one make a machine learn such dependencies? And how to understand who predicts better, 
the very clever house seller or the machine? 

For the first, you split the houses into two groups: **train** and **test** data. 
The first one is used to determine relations between features and price. 
The second one predicts the price for new houses, which are not in the first group. 
Thus, **building a model** is a sequence of methods you use to prepare and analyze data, find relations, 
and then predict new prices. 

The first step of capturing patterns from *train* data is called **fitting** or **training** the model. 
The data used to fit the model is called the **training data**. 
All the characteristics on which you base your decision are called **features**. 
For example, the number of Bedrooms or Bathrooms are features. And price is the **target**. 
Your simple algorithm in the case above may be as follows: 
“If a house has more than 2 Bedrooms then its price is $188000, else price is $178000”.

The details of how the model is *fitted* are complex enough and we will discuss it later. 
After the model has been fit, you can apply it to new or **test** data to **predict** prices of new houses. 
This will allow you to understand how good the model performs on unseen data, 
i.e. evaluate our model's performance. In most (though not all) applications, the relevant measure of model 
quality is predictive accuracy. In other words, will the model's predictions be close to what actually happens. 
There will be more theory about metrics later.

Therefore, we follow the next steps to build ML model:
1. Collect training data
2. Get features and target
3. Train (fit) model
4. Get predictions on new features from unseen part of dataset (test data)
5. Evaluate quality of the model

### ML algorithms

Now let’s talk about classification of algorithms. 
But first, we’ll give you a Tom Mitchell’s definition of machine learning:

*A computer program is said to learn from experience E with respect to some class of tasks T, 
and performance measure P, if its performance at tasks in T, as measured by P, improves with experience E.*

This definition is close to children’s *experience E* in school. 
From time to time the set of children learns and then repeats a multiplication table (*task T*) 
and gets grades (*performance measure P*) for knowledge. 
The more times children repeat a multiplication table, the more improved their knowledge becomes and better grades they achieve.

Thus, there are many kinds of machine learning, depending on the nature of the tasks T we wish the system to learn, 
the nature of the performance measure P we use to evaluate the system, and the nature of the training signal or experience 
E we give it. There is a great variety of ML methods. Let’s provide some examples.

|  | Task T | Performance measure P | Experience E |
| ----- | ------ | ------ | ----- |
| 1 | Predict house price | How close to the price we are | Description of every house in a city with fixed characteristics and price |
| 2 | Predict whether a client returns a loan | Is our prediction correct or not <br/><br/> Or the amount of money bank lost if provided a loan but the client has not return it | Salary of clients and their credit history |
| 3 | Predict when a patient needs to take medicine | Whether the medicine helps to recover | Current patient medical records. Performance of randomized control trial with this medicine. Plus the medical records of other patients. |
| 4 | Choose what medicine out of available a patient should take | Whether the medicine helps to recover | Current patient medical records. Performance of randomized control trials with these medicines. Plus the medical records of other patients |
| 5 | Choose segment of clients for a promo communication | Open rate of communication <br/><br/> Or increase in profit | The information of what items was included in the promo. Clients purchase history. Characteristics of products |
| 6 | Recognition of defective products on the production line (based on photo scans) | The amount of skipped defects | Photos of defective and non-defective products |
| 7 | Decide how to place products on a shelf in a store | The amount of products selled <br/><br/> Or  increase in profit | History of how we placed products before. Orders with products’ amounts. |
| 8 | Search sites for input text query | The ratio of successful searches <br/><br/> The mean rank of successful answer | Search queries of other users. Text description of every site |
| 9 | Split customers of a store into segments to understand differences of their behavior | How well you can interpret splits | Customers’ characteristics and purchase history |
| 10 | Detect anomaly in site traffic | The amount of prevented DDoS attacks | Stream of requests to your servers |

And these examples could be easily expanded with much more tasks. 
Furthermore, we can slightly change the incoming conditions of the task and it can require completely another solution. 
For instance, imagine if we need to conduct the promotion in the 5th example for absolutely new products from a new brand that do not have any history of purchases. 
Usually when a scientific field has a large variety in the tasks it tries to solve, 
then some classification is used to make it easier to navigate the tasks within. ML is no exception. 
The most important classification is into **supervised learning** and **unsupervised learning**.

#### Supervised learning 

Supervised learning is when you have some input variables (X) and an output variable (y) and you use an algorithm to learn the mapping function from the input to the output. The problem of housing price prediction is an example of supervised learning. 

It is called supervised learning because the process of an algorithm learning from the training dataset can be thought of as a teacher supervising the learning process. We know the correct answers, the algorithm iteratively makes predictions on the training data and is corrected by the teacher. Learning stops when the algorithm achieves an acceptable level of performance.

Supervised learning problems can be further grouped into regression and classification problems.

**Classification**. In classification problems, the output space is a set of _C_ unordered and mutually exclusive labels known as **classes** , $$Y = {1,2,...,C}$$. The problem of predicting the class label given an input is also called **pattern recognition**. (If there are just two classes, often denoted by $$y\in\{0,1\}$$ or $$y\in\{−1, +1\}$$, it is called _binary classification_.) A classification problem with several classes (greater than 2) is called _multiclass._ Also, there are a variety of multilabel problems.

For example, we use _binary classification_ to answer the question: has the patient a heart disease? _Multiclass classification_ is used in cases when each sample is assigned to one and only one label: a fruit can be either an apple or a pear or a banana but not both at the same time.

**Regression**. Suppose that we want to predict a real-valued quantity $$y ∈ R$$  instead of a class label $$y \in\{1,...,C\}$$; this is known as regression. See the example of housing price prediction above.

Think about what cases from the table above could also be formulated as a classification and regression task. Provide an answer inside the project notebook.

Unsupervised learning

In supervised learning we assume that each input example _x_ in the training set has an associated set of output targets _y_, and our goal is to learn the input-output mapping.

A much more interesting task is to try to "make sense of" data, as opposed to just learning a mapping. That is, we just get observed **inputs** $$D = \{x_i:i \in \{1, \dots, N\}$$ without any corresponding **output** $$y\_i **$$**. This is called unsupervised learning. In other words, Unsupervised learning is when you only have input data ($$X$$) and no corresponding output variables.

#### Unsupervised learning

In supervised learning we assume that each input example x in the training set has an associated set of output targets y, 
and our goal is to learn the input-output mapping.

A much more interesting task is to try to “make sense of” data, as opposed to just learning a mapping. 
That is, we just get observed **inputs** *D = {xn: n {1, ..., N}}* without any corresponding **output** *yn*. 
This is called unsupervised learning. In other words, 
Unsupervised learning is when you only have input data (X) and no corresponding output variables.

Unsupervised learning problems can be further grouped into **clustering**, **association** and **dimensionality reduction** problems.

**Clustering**: A clustering problem is where you want to discover the inherent groupings in the data, such as grouping customers by purchasing behavior. 

**Association**: An association rule learning problem is where you want to discover rules that describe large portions of your data, such as people that buy A also tend to buy B.

**Dimensionality reduction (or generalization)**: 
The aim of dimensionality reduction is to detect some common properties in our dataset and at the same time understand which features differ a lot. 
When we have too many features we can use such information to compress features to smaller amounts and not to lose crucial information inside. 
This trick is very useful when we need to visualize our dataset that have many features inside.

Think about what cases from the table above could be formulated as a clustering, association and dimensionality reduction task. 
Provide an answer inside the project solution. 
Please note that the boundary between unsupervised learning classes is not so clear in practice and all these tasks sometimes combine together. 
So feel free to share your opinion on how you can use these methods.

Thus, you know the basics of ML theory. The next step is practice.

## Chapter III. Goal

The goal of this project is to provide you with the basic understanding of how to build the simplest models. 
We will use the most popular methods of data analysis and processing, learn some methods of visualization. 
The result is an easy regression model to predict how popular an apartment rental listing is based on the 
listing content like text description, photos, number of bedrooms, price, etc.

## Chapter IV. Instructions

* This project will only be evaluated by humans. You are free to organize and name your files as you desire. 
* We recommend you push your local code into the Develop branch.
* Here and further, we use Python 3 as the only correct version of Python and recommend you to use JupyterNotebook.
* There are no strict rules for coding in this project. Nevertheless, you are asked to be clear and structured in the conception of your source code.
* Please observe the code culture: store data in the ‘data’ folder, move imports and functions to the beginning of the notebook, make plot captions, leave comments and make your code clear.

## Chapter V. Task

We will practice with a problem from Kaggle.com. Guiding instructions, you will predict the price of an apartment rental listing based on the listing content like text description, photos, number of bedrooms, price, etc. The data comes from renthop.com, an apartment listing website. 

Follow instructions, answer questions and get your final score!

1. Introduction. Write your answers in the *Intro* part of your Notebook 
   1. To get started, please write 5 examples of ML methods application in life. What is the benefit of using machine learning methods in each of your examples? 
   2. Use classification of tasks in the introduction to decide what class you can assign for the tasks from the table above and for the 5 examples you provided. 
   3. Please think and suppose, what is the difference between multiclass and multilabel.
   4. Is an example case with housing prices from theory a classification of a regression problem? Is it possible to reduce the regression problem to classification?
2. Intro data analysis
   1. Import libraries **pandas**, **numpy**, **sklearn**, **lightgbm**, **scipy**, **statsmodels**, **matplotlib**, **seaborn**. Use **pip install** if it’s necessary
   2. Load data from [kaggle](https://www.kaggle.com/competitions/two-sigma-connect-rental-listing-inquiries/data) with **pandas**. You are need only table data and **train.json**
   3. What is the size of your data? 
   4. Print the list of columns. Which column is a target? 
   5. Make a fast analysis of the data: use methods **info()**, **describe()**, **corr()**. Explain the results of outputs. Are there any empty columns? 
   6. We’ll work only with 3 features: 'bathrooms',  'bedrooms', 'interest_level' and with target column ‘price’. Make a dataframe with these columns only.
3. Statistical data analysis
   1. To start with statistical data analysis we recommend you refresh basic knowledge of statistics, such as Mean / Median / Mode / Variance / Standard Deviation. Also you are welcome to be free with distributions (Discrete uniform Distribution, Bernoulli Distribution, Binomial Distribution, Poisson Distribution, Normal Distribution, Exponential Distribution). Please make sure that you know the definitions of outliers, percentiles, confidential intervals. The article will be later 
   2. Make a quick sense with [this article](https://towardsdatascience.com/how-to-compare-two-or-more-distributions-9b06ee4d30bf). Please take attention to such aspects as distributions and histograms, boxplot, outliers, kernel density function.
   3. Target analysis
      1. Plot a histogram to understand the distribution of the target. Is it all clear? 
      2. The next step is boxplot(). What can you say about target? Are there any outliers? 
      3. Drop rows which are out of the 1 and 99 percentile by the target column. 
      4. Plot a histogram for price again. Explain the result.
   4. Features analysis
      1. What is the type of column 'interest_level'? 
      2. Print the values of this column. How many items each value contains? 
      3. Decode these values. For example, you may replace each value to 0, 1 or 2.
      4. Plot histograms for features 'bathrooms',  'bedrooms'. Are there outliers?
   5. Complex analysis
      1. Plot a correlation matrix to understand correlation between features and target. Plot a heatmap plot for correlation matrix. Is there a correlation? 
      2. Use a scatter plot to visualize correlation between features and target. You should return 3 plots, where X axis it target, and Y axis is a feature.
4. Generate features
   1. This step is very wide. You may create all features you want. For example, you may add 3 new features, which are squared: 'bathrooms_squared’, 'bedrooms_squared’, ‘'interest_level_squared'. Plot a correlation matrix with new features. Are new features more correlated with target then basic features? 
   2. To train model here we will not use your new features. Remember this example and use it in Lecture 2. To train the model, we will only consider 'bathrooms' and 'bedrooms' features.
   3. Read this sklearn info about PolynomialFeatures: https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html
   4. To use PolynomialFeatures we first need to split data to train and test samples. We already made it for you, please read the train and test data. 
   5. Initialize PolynomialFeatures() with the degree of 10. 
   6. Apply PolynomialFeatures() to fit and transform your train and test data.
5. Now you need to train 3 models: linear regression, decision tree and native model. We will use it as black boxes without deep understanding. 
   1. Result table. 
      1. Create two empty pandas DataFrames with columns ‘model’, ‘train’, ‘test’. Let’s the first be called result_MAE, and the second result_RMSE. We will fill these tables with results of models.
   2. Linear Regression 
      1. Initialize linear regression from **sklearn** without parameters. 
      2. Fit your model and make predict on train and test features. Save it as new columns in data 
      3. Calculate MAE (Mean Absolute Error) on train and test targets 
      4. Calculate RMSE (Root Mean Square Error) on train and test targets 
      5. Insert your metrics into tables *result_MAE* and *result_RMSE* with model name ‘linear_regression’
   3. Decision Tree
      1. Initialize decision tree regressor from sklearn with fixed random_state=42 
      2. Fit it on train features and train targe and make predict on train and test features. Save it as new column in data 
      3. Calculate MAE (Mean Absolute Error) on train and test targets 
      4. Calculate RMSE (Root Mean Square Error) on train and test targets 
      5. Insert your metrics into tables *result_MAE* and *result_RMSE* with model name ‘decision_tree’
   4. Native models
      1. Calculate mean and median of ‘price’ on train and test data and create a columns with these values 
      2. Calculate MAE on train and test targets between your target and calculated mean and median values 
      3. Calculate RMSE on train and test targets between your target and calculated mean and median values 
      4. Insert your metrics into tables result_MAE and result_RMSE with model names ‘native_mean’ and ‘native_median’
   5. Compare results 
      1. Print your final tables result_MAE and result_RMSE. 
      2. What is the best model?
   6. Additional
      1. You may practice with all data in your start dataset. Use and generate all features you want

### Submission

Save your code in python JupyterNotebook. Your peer will load it and compare with basic solution. 
Your code should contain the answers to all mandatory questions. Task ‘additional’ is on your own. 


>Please leave feedback on the project in the [feedback form.](https://forms.yandex.ru/cloud/646b43a8eb61462a4d084f0a/) 



