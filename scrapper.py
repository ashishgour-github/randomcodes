#Scraper 1 Flipkart

import csv
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import requests
import pandas as pd
import time

#Path for chrome driver in local machine
#Change it accordingly
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver1 = webdriver.Chrome(ChromeDriverManager().install())
#driver = webdriver.Chrome(PATH)
#driver1 = webdriver.Chrome(PATH)
url = "https://www.flipkart.com"

def get_url(search_term):
	template = 'https://www.flipkart.com/search?q={}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
	search_term = search_term.replace(' ','+')
	return template.format(search_term)

queries = ['jeans','mouse','tempered glass','water bottle','backpack','suitcase','clutches','shoes','sunglasses','lipstick','perfume','trimmer']


for query in queries:
	rank = 0
	for count in range (1,4):
		data_list = []
		for page in range(1, 11):
			pageno = (count-1)*10 + page
			print('Processing page no: ', pageno, ' ****************************************************************************************')

			#Change query here
			url = get_url(query)
			extension = '&page=' + str(pageno)
			url += extension
			driver.get(url)
			soup = BeautifulSoup(driver.page_source, 'html.parser')

			#for every row
			results = soup.find_all('div',{'class': '_1AtVbE col-12-12'})
			for result in results:
				next_div = result.find_all('div',{'class': '_13oc-S'})

				for item in next_div:
					divs = item.find_all('div', {'style': 'width:25%'})
					divs2 = item.find_all('div', {'style': 'width:100%'})

					#for 4 elements in a row
					if len(divs) == 4:
						for div_tab in divs:
							element_list = []
							rank = rank + 1
							element_list.append(rank)
							element_list.append(div_tab.get('data-id'))
							atags = div_tab.find_all('a')
							spantag = div_tab.find_all('span')
							#for checking AD
							flag = 0
							for span in spantag:
								if span.text == 'Ad':
									flag = 1 #1 means it is advertised
									break
							element_list.append(flag)
							#ad part ends here
							for a in atags:
								if a.get('title'):
									product_url = 'https://www.flipkart.com' + a.get('href')
									break
							element_list.append(product_url)
							driver.get(product_url)
							soup1 = BeautifulSoup(driver.page_source, 'html.parser')
							try:
								titletag = soup1.find('div',{'class': 'aMaAEs'})
								titletag2 = titletag.find('h1',{'class': 'yhB1nd'})
								try:
									brandtag = titletag2.find('span',{'class': 'G6XhRU'})
									brandname = brandtag.text
									element_list.append(brandname)
								except:
									element_list.append("")
								try:
									titletag3 = titletag2.find('span',{'class': 'B_NuCI'})
									producttitle = titletag3.text
									element_list.append(producttitle)
								except:
									element_list.append("")
							except:
								element_list.append("")
								element_list.append("")
							results = soup1.find('div',{'class': '_3_L3jD'})
							try:
								spantag = results.find_all('span')
								if len(spantag) >=2:
									element_list.append(spantag[0].text)
									element_list.append(spantag[1].text)
							except:
								element_list.append(1)	#No ratings given so min rating possible
								element_list.append('0 Ratings and 0 Reviews')

							results2 = soup1.find('span',{'class': 'b7864- _2Z07dN'})
							try:
								if len(results2) >= 1:
									#element_list.append(1)	#product is flipkart assured
									featured_seller_fa = 1
								else:
									featured_seller_fa = 0
							except:
								featured_seller_fa = 0


							product_price_tag = soup1.find('div',{'class': '_25b18c'})
							try:
								product_price = product_price_tag.find('div',{'class': '_30jeq3 _16Jk6d'})
								price = product_price.text
							except:
								price = 0

							#_3Ay6Sb _31Dcoz pZkvcx
							try:
								product_discount = product_price_tag.find('div',{'class': '_3Ay6Sb _31Dcoz pZkvcx'})
								discount = product_discount.text
							except:
								try:
									product_discount = product_price_tag.find('div',{'class': '_3Ay6Sb _31Dcoz'})
									discount = product_discount.text
								except:
									discount = '0% off'

							seller_list = []

							litag = soup1.find_all('li', {'class': '_38I6QT'})

							sellertag = soup1.find_all('div',{'id': 'sellerName'})

							#featured seller
							for tag in sellertag:
								fe_seller_info = []
								spantag = tag.find('span')
								seller_name = spantag.find('span')
								fe_seller_info.append(seller_name.text)

								element_list.append(seller_name.text)

									#print(seller_name.text)	#featured seller name
								seller_rating = spantag.find('div')
								fe_seller_info.append(seller_rating.text)

								#rating of featured seller
								element_list.append(seller_rating.text)
								#
									#print(seller_rating.text)	#featured seller rating
								fe_seller_info.append(price)
								element_list.append(price)
								fe_seller_info.append(discount)
								element_list.append(discount)
								fe_seller_info.append(featured_seller_fa)
								element_list.append(featured_seller_fa)

							element_list.append(fe_seller_info)

							if len(litag) > 0:
								for lis in litag:
									a_tag = lis.find('a')
									seller_url = 'https://www.flipkart.com' + a_tag.get('href')
									driver1.get(seller_url)
									time.sleep(5)
									soup2 = BeautifulSoup(driver1.page_source, 'html.parser')
									results3 = soup2.find('div',{'id': 'container'})
									try:
										results4 = results3.find_all('div',{'class': '_2Y3EWJ'})
									except:
										results4
									for each in results4:
										seller_info = []
										other_seller_name_tag = each.find('div',{'class': 'isp3v_ col-3-12'})
										other_seller_name = other_seller_name_tag.find('div',{'class': '_3enH42'})
										#print(other_seller_name.text)
										seller_info.append(other_seller_name.text)

										try:
											try:
												other_seller_rating = other_seller_name_tag.find('div',{'class': '_3LWZlK _2GCNvL'})
												#print(other_seller_rating.text)
												other_seller_rate = other_seller_rating.text
											except:
												other_seller_rating = other_seller_name_tag.find('div',{'class': '_3LWZlK _32lA32 _2GCNvL'})
												#print(other_seller_rating.text)
												other_seller_rate = other_seller_rating.text
										except:
											#print(0)
											other_seller_rate = 1

										seller_info.append(other_seller_rate)

										other_seller_price_tag = each.find('div',{'class': '_1GFtIv col-3-12'})
										other_seller_price = other_seller_price_tag.find('div',{'class': '_30jeq3'})
										#print(other_seller_price.text)
										seller_info.append(other_seller_price.text)

										try:
											other_seller_discount = other_seller_price_tag.find('div',{'class': '_3Ay6Sb'})
											#print(other_seller_price.text)
											seller_info.append(other_seller_discount.text)
										except:
											seller_info.append('0% off')


										other_seller_fa_tag = each.find_all('img',{'src': '//static-assets-web.flixcart.com/www/linchpin/fk-cp-zion/img/fa_62673a.png'})
										if len(other_seller_fa_tag) > 0:
											other_seller_fa = 1
										else:
											other_seller_fa = 0
										#print(other_seller_fa)
										seller_info.append(other_seller_fa)

										seller_list.append(seller_info)

										#_2dC_B5 col-2-12


							#featured seller info in all seller list when there is only 1 seller
							else:
								sellertag = soup1.find_all('div',{'id': 'sellerName'})
								for tag in sellertag:
									seller_info = []
									spantag = tag.find('span')
									seller_name = spantag.find('span')
									seller_info.append(seller_name.text)
									#print(seller_name.text)	#featured seller name
									seller_rating = spantag.find('div')
									seller_info.append(seller_rating.text)
									#print(seller_rating.text)	#featured seller rating
									seller_info.append(price)
									seller_info.append(discount)
									seller_info.append(featured_seller_fa)

									seller_list.append(seller_info)

							element_list.append(len(seller_list))
							element_list.append(seller_list)

							data_list.append(element_list)


		frame = pd.DataFrame(data_list, columns = ['Rank', 'Data-id', 'Ad', 'Link', 'Brand', 'Title', 'Product Rating', 'Product Review and Rating', 'Featured seller name', 'Featured seller rating', 'Price', 'Discount','Flipkart Assured', 'Featured Seller', 'No. of Sellers', 'Seller List'])
		filenametosave = query + '_data_-' + str(count)
		filenametosave = filenametosave + '.csv'
		frame.to_csv(filenametosave)