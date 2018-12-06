![TwitterFLightLogo](https://raw.githubusercontent.com/lawrencethomp/twitterFlight/master/workspace/twitterFlight/static/logo.png)  
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
Our data was taken from a Kaggle Dataset for the [Twitter US Airline Sentiments](https://www.kaggle.com/crowdflower/twitter-airline-sentiment). The dataset is a csv file from February 2015. Quoted from the original [project](https://www.figure-eight.com/data-for-everyone/):  

    A sentiment analysis job about the problems of each major U.S. airline. 
    Twitter data was scraped from February of 2015 and contributors were asked to first classify 
    positive, negative, and neutral tweets, followed by categorizing negative reasons (such as "late flight" or "rude service").



## The Filestructure:
- **data:** data for our backend. In the MVC (Model-View-Controller) paradigm, this would be the models.  
Tweets.csv: The data from [kaggle](https://www.kaggle.com/crowdflower/twitter-airline-sentiment)  
flightpickle.pkl: [Python object serial and de-serialization](https://pythontips.com/2013/08/02/what-is-pickle-in-python/), to convert into a byte stream for persistency.
[twitter_classification_notebook.ipynb](https://github.com/lawrencethomp/twitterFlight/blob/master/workspace/twitterFlight/data/twitter_classification_notebook.ipynb): The jupyter notebook for data exploration. Shows the use of SGD Classifier.  

- static  
**logo.png:** The logo to our project, shown on the webapp.

- **templates:** TwitterFlight uses [Flask](http://flask.pocoo.org/), a Python microframework, to handle its webapp component. Templates are how the data is presented. The frontend uses Materialize and JQuery to handle the presentation for an enhanced user experience.  
formhelpers.html: Handles forms and error presentation.  
analysis.html: shows the results of the analysis.  
main.html: Allows the user to create a tweet and see if the process can be replicated.  

- **root:** contains the main files for the application, and some stuff for git.  
    .gitignore: Specifies intentionally untracked files to ignore.  
    Tweets.csv: The data from [kaggle](https://www.kaggle.com/crowdflower/twitter-airline-sentiment)  
    [app.py](https://github.com/lawrencethomp/twitterFlight/blob/master/workspace/twitterFlight/app.py): The main file for the Flask application.   
    database.sqlite: sqlite database for user-created tweets.   
    flightPickle.pkl: pickled data for persistence.  
    [form.py](https://github.com/lawrencethomp/twitterFlight/blob/master/workspace/twitterFlight/form.py): Login for Flask.  
    [requirements.txt](https://github.com/lawrencethomp/twitterFlight/blob/master/workspace/twitterFlight/requirements.txt): [Easy install](https://stackoverflow.com/questions/7225900/how-to-install-packages-using-pip-according-to-the-requirements-txt-file-from-a) for pip files, use _pip install -r /path/to/requirements.txt_.  
    [stats.py](https://github.com/lawrencethomp/twitterFlight/blob/master/workspace/twitterFlight/stats.py): returns consensus on the airline according to positive, negative, or neutral sentiments.   
