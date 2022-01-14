import csv
import pandas as pd

queries = ['clutches','shoes for boys','sunglasses','lipstick','perfume','suitcase','trimmer']


for query in queries:

	d = {}
	won = {}
	new_list = []
	for number in range(1, 4):
		filename = query+'_data_-'+str(number)+'.csv'
		with open(filename, encoding="utf8") as csv_file:
			csv_reader = csv.reader(csv_file)
			print(query)
			next(csv_reader) #jump to 2nd line OR ignore first line.

			for line in csv_reader:
				#print(line[1])
				item_list=[]
				item_list.append(line[1])	#Rank
				item_list.append(line[2])	#Data-id

				end = len(line[6])
				string = line[6][0:end]
				string = string.replace("\"", '')
				li = list(string.split(" "))
				#item_list.append(line[6])	#title

				#private label?
	#			if li[0] == 'Flipkart' and li[1]=='SmartBuy':
	#				item_list.append(1)
	#			else:
	#				item_list.append(0)

				#item_list.append(line[5])	#brand
				if line[5] == 'METRONAUT':
					item_list.append(1)
				elif line[5] == 'METRONAUT ':
					item_list.append(1)
				elif line[5] == 'METRONAUTÂ ':
					item_list.append(1)
				elif line[5] == 'Divastri':
					item_list.append(1)
				elif line[5] == 'DivastriÂ ':
					item_list.append(1)
				elif line[5] == 'Divastri ':
					item_list.append(1)
				elif line[5] == 'CARA MIA':
					item_list.append(1)
				elif line[5] == 'CARA MIAÂ ':
					item_list.append(1)
				elif line[5] == 'CARA MIA ':
					item_list.append(1)
				elif line[5] == 'Ann Springs':
					item_list.append(1)
				elif line[5] == 'Ann SpringsÂ ':
					item_list.append(1)
				elif line[5] == 'Ann Springs ':
					item_list.append(1)
				elif line[5] == 'Miss & Chief':
					item_list.append(1)
				elif line[5] == 'Miss & ChiefÂ ':
					item_list.append(1)
				elif line[5] == 'Miss & Chief ':
					item_list.append(1)
				elif line[5] == 'Anmi':
					item_list.append(1)
				elif line[5] == 'AnmiÂ ':
					item_list.append(1)
				elif line[5] == 'Anmi ':
					item_list.append(1)
				elif line[5] == 'Flipkart SmartBuy':
					item_list.append(1)
				elif line[5] == 'Flipkart SmartBuyÂ ':
					item_list.append(1)
				elif line[5] == 'Flipkart SmartBuy ':
					item_list.append(1)
				elif line[5] == 'SmartBuy':
					item_list.append(1)
				elif line[5] == 'SmartBuyÂ ':
					item_list.append(1)
				elif line[5] == 'SmartBuy ':
					item_list.append(1)
				elif line[5] == 'Digiflip':
					item_list.append(1)
				elif line[5] == 'DigiflipÂ ':
					item_list.append(1)
				elif line[5] == 'Digiflip ':
					item_list.append(1)
				elif line[5] == 'Citron':
					item_list.append(1)
				elif line[5] == 'CitronÂ ':
					item_list.append(1)
				elif line[5] == 'Citron ':
					item_list.append(1)
				else:
					item_list.append(0)

				#item_list.append(line[9])	#featured seller
				#alpha seller?
				if line[9] == 'RetailNet':
					item_list.append(1)
				elif line[9] == 'HydtelRETAILSsales':
					item_list.append(1)
				elif line[9] == 'OmniTechRetail':
					item_list.append(1)
				elif line[9] == 'SuperComNet':
					item_list.append(1)
				else:
					item_list.append(0)
				item_list.append(line[3])	#Ad?
				item_list.append(line[7])	#Product rating
				if(line[10]=='(New Seller)'):
					item_list.append('1')
				elif(line[10]=='(Not Enough Ratings)'):
					item_list.append('1')
				else:
					item_list.append(line[10])	#Featured seller rating
				if(line[13]==''):
					item_list.append('0')
				else:
					item_list.append(line[13])	#Flipkart Assured?
				
				end = len(line[11])
				string = line[11][0:end]
				string = string.replace(",", '')
				string = string.replace("â‚¹", '')
				string = string.replace("₹", '')
				item_list.append(string)	#price

				end = len(line[12])
				string = line[12][0:end]
				string = string.replace("%", '')
				li = list(string.split(" "))
				item_list.append(li[0])	#discount

	#			print(line[1])
				new_list.append(item_list)
#				pid = line[2]
#				if pid in d:
#					d[pid]=d[pid]+1
#				else:
#					d[pid]=1
#					new_list.append(item_list)

	frame = pd.DataFrame(new_list, columns = ['Rank', 'Data-id', 'PL?', 'Alpha Seller?', 'Ad?', 'Product Rating', 'Seller Rating', 'Flipkart Assured?', 'Price', 'Discount'])
	filenametosave=query+'_analysis_1nov_1.csv'
	frame.to_csv(filenametosave)