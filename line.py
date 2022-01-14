import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
from sklearn.pipeline import Pipeline
from sklearn.metrics import ndcg_score
import csv

queries = ['clutches','shoes for boys','sunglasses','lipstick','perfume','suitcase','trimmer']
new_list_pl = []
new_list_as = []

for query in queries:

    item_list_pl=[]
    item_list_as=[]
    item_list_pl.append(query)
    item_list_as.append(query)
    pipeline = Pipeline([('scaler', StandardScaler()), ('estimator', SVR(kernel="linear"))])
    filename = query+'_analysis.csv'
    with open(filename, encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file)
        #print(query)
        next(csv_reader) #jump to 2nd line OR ignore first line.
        lineno = 1

        for line in csv_reader:
            lineno = lineno + 1

        print(lineno)
        item_list_pl.append(lineno)

    new_list_pl.append(item_list_pl)

frame = pd.DataFrame(new_list_pl, columns = ['query', 'line'])
filenametosave='0_line.csv'
frame.to_csv(filenametosave)