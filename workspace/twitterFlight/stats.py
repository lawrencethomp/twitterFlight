# Before we begin, we supress deprecation warnings resulting from nltk on Kaggle
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 


import matplotlib.pyplot as plt, mpld3
import matplotlib.style
from matplotlib.pyplot import subplots

import pandas as pd
tweets = pd.read_csv("Tweets.csv")
list(tweets.columns.values)

sentiment_counts = data.airline_sentiment.value_counts()
number_of_tweets = data.tweet_id.count()
dff = data.groupby(["airline", "airline_sentiment" ]).count()["name"]
df_companySentiment = dff.to_frame().reset_index()
df_companySentiment.columns = ["airline", "airline_sentiment", "count"]
df2 = df_companySentiment
df2.index = df2['airline']
del df2['airline']
matplotlib.style.use('ggplot')

fig, ax = subplots()
my_colors =['darksalmon', 'papayawhip', 'cornflowerblue']
df2.plot(kind='bar', stacked=True, ax=ax, color=my_colors, figsize=(12, 7), width=0.8)
ax.legend(["Negative", "Neutral", "Positive"])
plt.title("Tweets Sentiments Analysis Airlines, 2017")
#mpld3.show()