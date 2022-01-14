import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeRegressor 
from scipy.stats import spearmanr
from scipy.stats import kendalltau


dataset = pd.read_csv('Nykaa_Sunglasses_2.csv')
dataset

x = dataset.iloc[:30,1:]
y = dataset.iloc[:30,:1]
x


x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3,random_state=42)



x_train = x_train.sort_index()
y_train = y_train.sort_index()
for i in range(len(y_train)) :
    y_train.iloc[i, 0] = i+1
x_test = x_test.sort_index()
y_test = y_test.sort_index()
for i in range(len(y_test)) :
    y_test.iloc[i, 0] = i+1


  
# create a regressor object
regressor = DecisionTreeRegressor(random_state = 0) 
  
# fit the regressor with X and Y data
regressor.fit(x_train,y_train)

y_pred = regressor.predict(x_test)


# In[101]:

y_pred

z = np.c_[y_pred, 1:224 ]
x = z[z[:, 0].argsort()]
w = np.c_[x, 1:224 ] 
a , b = w[:,1], w[:,2]


mse = mean_squared_error(a,b)
rsquare = np.sqrt(mse)
rsquare

coef, p = spearmanr(b, a)

print('Spearmans correlation coefficient: %.3f' % coef)
alpha = 0.05
if p > alpha:
    print('Samples are uncorrelated (fail to reject H0) p=%.3f' % p)
else:
    print('Samples are correlated (reject H0) p=%.3f' % p)
    
coef, p = kendalltau(b, a)

print('Kendall correlation coefficient: %.3f' % coef)
alpha = 0.05
if p > alpha:
    print('Samples are uncorrelated (fail to reject H0) p=%.3f' % p)
else:
    print('Samples are correlated (reject H0) p=%.3f' % p)