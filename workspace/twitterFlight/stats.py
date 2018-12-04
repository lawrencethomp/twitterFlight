# Before we begin, we supress deprecation warnings resulting from nltk on Kaggle
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 


import matplotlib.pyplot as plt, mpld3
import matplotlib.style
from matplotlib.pyplot import subplots

import pandas as pd

def groupairline(airline):
	tweets = pd.read_csv("Tweets.csv")
	t_gb = tweets.groupby(["airline", "airline_sentiment" ]).count()["name"]
	df_airlineSentiment = t_gb.to_frame().reset_index()
	df_airlineSentiment.columns = ["airline", "airline_sentiment", "count"]
	df = df_airlineSentiment
	del df['airline']
	if airline == 'US':
		airline = 'US Airways'
	return t_gb[airline,'positive'], t_gb[airline,'negative'], t_gb[airline,'neutral']