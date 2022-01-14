import csv
import pandas as pd

queries = ['clutches','lipstick','perfume','suitcase','sunglasses','trimmer']
#queries = ['backpack']

for query in queries:

	d = {}
	won = {}
	pl = {}
	alphas = {}
	data_list = []
	datelist = ['1nov_1','1nov_2','1nov_3','1nov_4','3nov_1','3nov_2','3nov_3','3nov_4','5nov_1','5nov_2','5nov_3','5nov_4','7nov_1','7nov_2','7nov_3','7nov_4','9nov_1','9nov_2','9nov_3','9nov_4','11nov_1','11nov_2','11nov_3','11nov_4']
	for number in datelist:
		filename = query+'_analysis_'+number+'.csv'
		print(filename)
		try:
		    with open(filename, encoding="utf8") as csv_file:
		    	csv_reader = csv.reader(csv_file)
		    	next(csv_reader)
		    	for line in csv_reader:

		    		pid = line[2]
		    		if pid in d:
		    			d[pid]=d[pid]+1
		    		else:
		    			d[pid]=1
		    			pl[pid]=int(line[3])
		    			alphas[pid]=int(line[4])

		except IOError:
		    print("File not accessible")
				
	for x,y in d.items():
		if y>1:
			element_list = []
			element_list.append(x)
			element_list.append(y)
			element_list.append(pl[x])
			element_list.append(alphas[x])
			data_list.append(element_list)

	frame = pd.DataFrame(data_list, columns = ['ID', 'Count','PL?', 'Alpha Seller'])
	filenametosave=query+'_multiple.csv'
	frame.to_csv(filenametosave)