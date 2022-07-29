import numpy as np 
import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier 

print("====================0===================")
df= pd.read_csv('C:/Users/Uzer/Desktop/S8/2Machine Learning/py code/dataSets/CreditScoring.csv')
print(df.isnull().sum())

print("====================1===================")
#remplir les cases vides par la moyenne
df.fillna(value=df.mean(),inplace=True)
print(df.isnull().sum())

#removing the features BAD,JOB,REASON
x_basic= df.drop(columns=['BAD','JOB','REASON'])
y=df['BAD']

print("====================2===================")
print(df.isnull().sum())
x_basic_tr,x_basic_te,y_tr,y_te=train_test_split(x_basic,y, test_size=.33, random_state=1)

model=DecisionTreeClassifier()
model.fit(x_basic_tr,y_tr)
y_pre=model.predict(x_basic_te)
a=accuracy_score(y_te, y_pre)
print("accuracy score: ",a)

#to draw the decision tree
"""
from six import StringIO
from IPython.display import Image  
from sklearn.tree import export_graphviz
import pydotplus

dot_data = StringIO()

feature_names=x_basic.columns[:]
#print(feature_names)
class_names=['0','1']
export_graphviz(model, out_file=dot_data,filled=True, 
                rounded=True,special_characters=True,
                feature_names=feature_names ,  
                class_names=class_names)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
svg_graph = graph.create_svg()
svg = open('gini_tree.svg', 'wb')
svg.write(svg_graph)
svg.close()
Image(graph.create_png())"""