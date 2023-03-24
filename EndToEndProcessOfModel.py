import pandas as pd

df=pd.read_csv("/content/testdata.csv")

df

df.info()

df.shape

df.head()

import matplotlib.pyplot as plt

plt.scatter(df["CGPA"],df["IQ"],c=df["PLACEMENTS"])

X=df.iloc[:,0:2]
Y=df.iloc[:,-1]

X

Y

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.1)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_train

X_test = scaler.transform(X_test)
X_test

from sklearn.linear_model import LogisticRegression
clf = LogisticRegression()

#Model Training
clf.fit(X_train,Y_train)

Y_pred = clf.predict(X_test)
Y_pred

Y_test

from sklearn.metrics import accuracy_score

accuracy_score(Y_test,Y_pred)

from mlxtend.plotting import plot_decision_regions

plot_decision_regions(X_train,Y_train.values,clf=clf,legend=2)

import pickle

pickle.dump(clf,open('model.pkl','wb'))