# TwitterFlight
A classification project by Oreva and Lawrence

## Why we're doing this project
People like to complain about things on Twitter. A lot. Next to trying to launch careers as comedians or pundits, there are somewhere around a million people and companies to complain to. With all these complaints and [often from the best of them](https://www.thewrap.com/john-podhoretz-declares-victory-in-war-with-nyc-restaurant-chain/), it poses the question: can we take a bunch of comments from Twitter's best, most vocal, and brightest, and make predictions on whether they what they were saying?

## The Assignment:
Taken from [here](https://mycourses.unh.edu/courses/48074/assignments/306480)
- Must use a Classification technique 
- Must use a real data set (not fake data set, i.e. randomly generated numbers) 
- Must have Juypter Notebook Documentation
- Do exploratory data exploration using graphs  (5%)
- Explain the tradeoffs you made in feature engineering and feature selection. (10%)
- Explain the tradeoffs you made in model selection. Include how you choose the model and how you tune the hyper-parameters.  (10%)
- Must explain in detail how you evaluate the accuracy of model (10%)

## The Data:
Our data was taken from a Kaggle Dataset for the Twitter US Airline https://www.kaggle.com/crowdflower/twitter-airline-sentiment

## The Filestructure:
- data  
Tweets.csv: The data from [kaggle](https://www.kaggle.com/crowdflower/twitter-airline-sentiment)  
flightpickle.pkl: [Python object serial and de-serialization](https://pythontips.com/2013/08/02/what-is-pickle-in-python/), to convert into a byte stream for persistency.
[twitter_classification_notebook.ipynb](https://github.com/lawrencethomp/twitterFlight/blob/master/workspace/twitterFlight/data/twitter_classification_notebook.ipynb): The jupyter notebook for data exploration. Shows the use of SGD Classifier.  
- static  
logo.png: The logo to our project, shown on the webapp.
- templates    
.gitignore  
Tweets.csv  
app.py  
database.sqlite  
flightPickle.pkl  
form.py  
requirements.txt  
stats.py  
