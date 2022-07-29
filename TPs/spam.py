import numpy as np
import pandas
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression    

spams = pandas.read_table("C:\\SMSSpamCollection.txt",sep="\t",header=0)
spamsTrain, spamsTest = train_test_split(spams,train_size=0.7,random_state=1)
 
parseur = CountVectorizer()
Xtrain = parseur.fit_transform(spamsTrain['message'])
mdtTrain = Xtrain.toarray()
 


modelFirst = LogisticRegression()

modelFirst.fit(mdtTrain,spamsTrain['classe'])
score1=modelFirst.score(mdtTrain,spamsTrain['classe'])
print("score sur data train :"+str(score1))
mdtTest = parseur.transform(spamsTest['message'])
score2=modelFirst.score(mdtTest,spamsTest['classe'])
print("score sur data test : "+str(score2))