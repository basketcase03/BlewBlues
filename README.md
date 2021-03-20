# BlewBlues
## Prediction of Depression induced by the COVID-19 pandemic in individuals

### Problem Statement
COVID-19 has caused some drastic changes in our lifestyles, coupled with restrictions, quarantines, and social distancing measures, that have to lead to many social health issues all over the world. According to the findings made by WHO, depression is most common among them. Therefore, it becomes very important to prevent mental health disorders by early prediction of individuals at a higher risk due to high distress during the COVID-19 pandemic.

### Approach
The project involves building a depression detection system that can analyze the level of depression in an individual and then suggest to use a self-care chatbot, if signs of depression are detected. It requires a computation of relevant physiological predictor features, and machine learning analysis of highly heterogeneous data. The objective is to identify potential depression in the users and then offer suitable support and assist them to a path of recovery.

Broadly, Our approach to the problem involves the following steps: 
+ Using relevant features
+ detect if a person may have depression
+ Identify the vulnerable groups 
+ Provide elementary assistance

This can be done in the following steps: 
+ Collecting relevant data 
+ Making suitable models 
+ Compare them effectively 
+ Deploying the model

### Flow of solution
Dataset: It has been noticed that some people turn to social media to outlet their thoughts and emotions, which can entice the user to be more uninhibited in their expressions. This creates an incentive based on their tweets for emotional detection of users. So, initially we will use data from existing sources and then, we will filter out the tweets containing depressive and non-depressive hashtags. This way the model will be more sensitive to the content and more precise in its predictions as we have distinguished the tweets based on its content rather than tags.

The proposed approach is divided into following steps:

#### Collecting user history: 
To get an input for our model, we need the user's search history over a period of time as depression can be detected by analyzing the language that people use to express themselves.

#### Feature extraction: 
We will extract various psycholinguistic measurements from it to identify and demonstrate depressive and non-depressive content. LIWC is a psycholinguistic vocabulary kit developed by psychological analysts to perceive the various affective, intellectual, and etymological components that lie in the verbal or written correspondence of a person. This brings back more than 70 different variables with higher psycholinguistic characteristics. We will take some of these factors and change over every depressive and non-depressive content into numerical values in view of psycholinguistic features.

#### Classification model: 
The problem can be identified as sentiment analysis which is a classification task in Natural Language Processing (NLP). So, we will be building a simple GRU model with concat pooling which is similar to LSTM, but incorporates faster learning and more memory efficiency. The implementation can easily be done using TorchText. We will compare this approach to other approaches, and look into more ways including different models or combinations of them.

#### Providing elementary assistance: 
If symptoms of depression have been found, the self-care bot recommendation may be an automated function that is incorporated into the identification of depression, and the raw data does not need to go back to the centralised server and does not require the identity of the user to be revealed. Federated learning and local differential privacy can be applied here to ensure that the privacy of the user is secured.

### Technology Stack: Python, Google Colab, TorchText, Tensorflow.

### Current status and Entrepreneurial scope:
There are not many technologies that can help people battle mental health problems because there was hardly any awareness about such issues. It is only recently that people have started getting more aware about this topic and there is potential for a huge area of research as the advent of technology and global pandemic lead and increase isolation to the inbuilt gregarious human beings.

This project could be the foundation of formation of an organisation that helps people cope with the mental problems day to day. It could also help connect various clinical psychologists and can also grow to serve as a place where people tend to seek and give advice on mental health. It can grow into a community and it would act to increase awareness about depression, help identify groups vulnerable to depression and provide support to people.


