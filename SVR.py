import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR

dataset = pd.read_csv('Downloads/shoes for boys - Updated.csv')
dataset

df = pd.DataFrame(dataset)
#df = df.drop(columns=['noOfReview','discount'])
dataset=df
dataset

x = dataset.iloc[:,1:]
y = dataset.iloc[:,:1]

st_x=StandardScaler()
st_y=StandardScaler()

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3,random_state=42,stratify=df[['PL?','Ad?','Alpha Seller?']])

x_train = x_train.sort_index()
x_train

y_train = y_train.sort_index()
for i in range(len(y_train)) :
    y_train.iloc[i, 0] = i+1
y_train


x_test = x_test.sort_index()
x_test

y_test = y_test.sort_index()
for i in range(len(y_test)) :
    y_test.iloc[i, 0] = i+1
y_test

x_train=st_x.fit_transform(x_train)
y_train=st_y.fit_transform(y_train)
x_test=st_x.fit_transform(x_test)
y_test=st_y.fit_transform(y_test)


regressor=SVR(kernel='linear')

fit = regressor.fit(x_train,y_train)

y_pred = regressor.predict(x_test)

mse = mean_squared_error(y_test,y_pred)
rsquare = np.sqrt(mse)
rsquare

fit.intercept_
fit.coef_ 
y_pred
y_test

#y_train.join(x_train)