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
        print(query)
        next(csv_reader) #jump to 2nd line OR ignore first line.
        lineno = 1
        nextstop = 2

        prevpl=0
        prevas=0
        sumpl=0
        sumas=0

        for line in csv_reader:

            #PL is on column 2(0 indexed)
            #AS is on column 3

            if line[2]==1 or line[2]=='1':
                sumpl+=1
            if line[3]==1 or line[3]=='1':
                sumas+=1

            if lineno == nextstop:
                nextstop = nextstop*2
                item_list_pl.append(sumpl-prevpl)
                item_list_as.append(sumas-prevas)
                prevpl=sumpl
                prevas=sumas
            lineno = lineno + 1

        item_list_pl.append(sumpl-prevpl)
        item_list_as.append(sumas-prevas)
    

    new_list_pl.append(item_list_pl)
    new_list_as.append(item_list_as)

frame = pd.DataFrame(new_list_pl, columns = ['query', '1-2', '3-4', '5-8', '9-16', '17-32', '33-64', '65-128', '129-256', '257-512', '513-'])
filenametosave='0_brackets_pl.csv'
frame.to_csv(filenametosave)

frame = pd.DataFrame(new_list_as, columns = ['query', '1-2', '3-4', '5-8', '9-16', '17-32', '33-64', '65-128', '129-256', '257-512', '513-'])
filenametosave='0_brackets_as.csv'
frame.to_csv(filenametosave)