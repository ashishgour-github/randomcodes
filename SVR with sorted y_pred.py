import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
from sklearn.pipeline import Pipeline

pipeline = Pipeline([('scaler', StandardScaler()), ('estimator', SVR(kernel="linear"))])

dataset = pd.read_csv('Downloads/shoes for boys - Updated.csv')
dataset

df = pd.DataFrame(dataset)
dataset=df
dataset

x = dataset.iloc[:,1:]
y = dataset.iloc[:,:1]

st_x=StandardScaler()
st_y=StandardScaler()

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3,random_state=42,stratify=df[['PL?','Ad?']])

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
#y_test=st_y.fit_transform(y_test)


#regressor=SVR(kernel='linear')

#fit = regressor.fit(x_train,y_train)

fit = pipeline.fit(x_train,y_train)

y_pred = st_y.inverse_transform(pipeline.predict(x_test))

#mse = mean_squared_error(y_test,y_pred)
#rsquare = np.sqrt(mse)
#rsquare

#fit.intercept_
#fit.coef_ 
#y_pred
#y_test

z = np.c_[y_pred, 1:224 ]
x = z[z[:, 0].argsort()]
w = np.c_[x, 1:224 ] 
a , b = w[:,1], w[:,2]

mse = mean_squared_error(a,b)
rsquare = np.sqrt(mse)
rsquare

#rbf => 72.470
#linear => 71.261


#extra

st_a=StandardScaler()
st_b=StandardScaler()


a_new = np.reshape(a,(223,1))
b_new = np.reshape(b,(223,1))
a_new=st_a.fit_transform(a_new)
b_new=st_b.fit_transform(b_new)
mse = mean_squared_error(a_new,b_new)
rsquare = np.sqrt(mse)
rsquare



#corelation

from scipy.stats import spearmanr
from scipy.stats import kendalltau

coef, p = spearmanr(y_test, y_pred)

print('Spearmans correlation coefficient: %.3f' % coef)
alpha = 0.05
if p > alpha:
    print('Samples are uncorrelated (fail to reject H0) p=%.3f' % p)
else:
    print('Samples are correlated (reject H0) p=%.3f' % p)
    
coef, p = kendalltau(y_test, y_pred)

print('Kendall correlation coefficient: %.3f' % coef)
alpha = 0.05
if p > alpha:
    print('Samples are uncorrelated (fail to reject H0) p=%.3f' % p)
else:
    print('Samples are correlated (reject H0) p=%.3f' % p)