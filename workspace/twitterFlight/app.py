from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,Form, TextAreaField, validators, SelectField, TextField, IntegerField, RadioField
from wtforms.validators import DataRequired
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
import re
from nltk.stem.porter import PorterStemmer
import nltk
from nltk.corpus import stopwords
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import SGDClassifier
from stats import groupairline
import pickle

app = Flask(__name__)


def preprocessor(text):
    text = re.sub('<[^>]*>', '', text)
    emoticons = re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P)',
                           text)
    text = (re.sub('[\W]+', ' ', text.lower()) +
            ' '.join(emoticons).replace('-', ''))
    return text
    
porter = PorterStemmer()
nltk.download('stopwords')

def tokenizer_porter(text):
    return [porter.stem(word) for word in text.split()]

def tokenizer(text):
    return text.split()

def train_classify():
	data = pd.read_csv('Tweets.csv', encoding='utf-8')	
	data['text'] = data['text'].apply(preprocessor)
	stop = stopwords.words('english')
	X_train = data.iloc[:2000, 0].values
	y_train = data.iloc[:2000, 1].values
	X_test = data.iloc[2000:4000, 0].values
	y_test = data.iloc[2000:4000, 1].values
	tfidf = TfidfVectorizer(strip_accents=None,
                        lowercase=False,
                        preprocessor=None)
	param_grid = [{'vect__ngram_range': [(1, 1)],
               'vect__tokenizer': [tokenizer, tokenizer_porter],
               'vect__stop_words': [stop, None]},
              ]
              
	lr_tfidf = Pipeline([('vect', tfidf),
                    ('sgd', SGDClassifier(random_state=0))])

	gs_lr_tfidf = GridSearchCV(lr_tfidf, param_grid,
                           scoring='accuracy',
                           cv=5,
                           verbose=1)
	gs_lr_tfidf.fit(X_train, y_train)
	clf = gs_lr_tfidf.best_estimator_
	mypickle_path = 'flightPickle.pkl'
	flightpickle = open(mypickle_path, 'wb')
	pickle.dump(clf, flightpickle)
	flightpickle.close()

train = train_classify()

def unpickle():
	mypickle_path = 'flightPickle.pkl'
	model_unpickle = open(mypickle_path, 'rb')
	clf_new = pickle.load(model_unpickle)
	return clf_new

class flightForm(Form):
	submit = SubmitField("Send")
@app.route("/")
def hello():
	form = flightForm(request.form)
	return render_template('main.html', form=form)

@app.route('/analysis', methods=['POST'])
def result():
    form = flightForm(request.form)
    if request.method == 'POST' and form.validate():
        review = request.form['sentimentTextarea']
        airline = request.form['airline']
        myname = request.form['nameText']
        review_this = unpickle()
        category = review_this.predict([review])
        currentairlinedata = groupairline(airline)
        americandata =  airlinedata = groupairline('American')
        deltadata =  airlinedata = groupairline('Delta')
        southwestdata =  airlinedata = groupairline('Southwest')
        uniteddata =  airlinedata = groupairline('United')
        usdata =  airlinedata = groupairline('US')
        vadata =  airlinedata = groupairline('Virgin America')
        return render_template('analysis.html',
                                category=category[0], myname=myname, airline=airline,
                                currentpositive=currentairlinedata[0],
                                currentnegative=currentairlinedata[1],currentneutral=currentairlinedata[2],
                                americanpositive=americandata[0],
                                americannegative=americandata[1],americanneutral=americandata[2],
                                deltapositive=deltadata[0],
                                deltanegative=deltadata[1],deltaneutral=deltadata[2],
                                southwestpositive=southwestdata[0],
                                southwestnegative=southwestdata[1],southwestneutral=southwestdata[2],
                                unitedpositive=uniteddata[0],
                                unitednegative=uniteddata[1],unitedneutral=uniteddata[2],
                                uspositive=usdata[0],
                                usnegative=usdata[1],usneutral=usdata[2],
                               	vapositive=vadata[0],
                                vanegative=vadata[1],vaneutral=vadata[2])
    return render_template('reviewform.html', form=form)
    
if __name__ == "__main__":
    app.run(debug=True)