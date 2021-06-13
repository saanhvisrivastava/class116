# -*- coding: utf-8 -*-
"""class116.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15n70huAmSKpuC31V2R3ffxG1ktnw9jQH
"""

import csv
import pandas as pd
import plotly.express as px

df=pd.read_csv('data116.csv')

hours_slept=df['Hours_Slept'].tolist()
hours_studied=df['Hours_studied'].tolist()

fig=px.scatter(x=hours_slept,y=hours_studied)
fig.show()

import csv
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df=pd.read_csv('data116.csv')

hours_slept=df['Hours_Slept'].tolist()
hours_studied=df['Hours_studied'].tolist()
results=df['results'].tolist()

colors=[]

for i in results:
  if i==1:
    colors.append('green')
  else:
    colors.append('red')

fig=go.Figure(data=go.Scatter(
    x=hours_slept,
    y=hours_studied,
    mode='markers',
    marker=dict(color=colors)
))
fig.show()

import csv
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df=pd.read_csv('data116.csv')

hours_slept=df['Hours_Slept'].tolist()
hours_studied=df['Hours_studied'].tolist()
results=df['results'].tolist()


factors=df[['Hours_Slept','Hours_studied']]
result=df['results']

print(result)



from sklearn.model_selection import train_test_split

slept_train,slept_test,result_train,result_test=train_test_split(factors,result,test_size=0.25,random_state=0)
print(slept_train)

from sklearn.linear_model import LogisticRegression

classifier=LogisticRegression(random_state=0)
classifier.fit(slept_train,result_train)

result_pred=classifier.predict(slept_test)

from sklearn.metrics import accuracy_score

print('accuracy:',accuracy_score(result_test,result_pred))

from sklearn.preprocessing import StandardScaler

sc_x=StandardScaler()
slept_train=sc_x.fit_transform(slept_train)

hours_studied=int(input('Enter hours studied'))
hours_slept=int(input('Enter hours slept'))

user_test=sc_x.transform([[hours_slept,hours_studied]])
user_pred=classifier.predict(user_test)

if user_pred[0]==1:
  print('User will pass')
else:
  print('User may not pass')