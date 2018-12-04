# Before we begin, we supress deprecation warnings resulting from nltk on Kaggle
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 


import matplotlib.pyplot as plt, mpld3
import matplotlib.style
from matplotlib.pyplot import subplots

import pandas as pd

def groupairline(airline):
	tweets = pd.read_csv("Tweets.csv")
	list(tweets.columns.values)

	sentiment_counts = tweets.airline_sentiment.value_counts()
	number_of_tweets = tweets.tweet_id.count()
	dff = tweets.groupby(["airline", "airline_sentiment" ]).count()["name"]
	df_companySentiment = dff.to_frame().reset_index()
	df_companySentiment.columns = ["airline", "airline_sentiment", "count"]
	df2 = df_companySentiment
	del df2['airline']
	if airline == 'US':
		airline = 'US Airways'
	return dff[airline,'positive'], dff[airline,'negative'], dff[airline,'neutral']