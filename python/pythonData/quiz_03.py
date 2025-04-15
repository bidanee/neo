import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'NanumBarunGothic'

url = 'https://www.moviechart.co.kr/rank/boxoffice'
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

infos = soup.find_all('div',attrs={'class': 'listTable'})
# print(infos)

mydata1 = [i for i in range(1,21)]

result = []
title = soup.select('td.title')
for i in title:
  result.append((i.text).replace('\n',''))
mydata2 = result
# print(mydata2)

result = []
date = soup.select('td.date')
for i in date:
  result.append(i.text)
mydata3 = result
# print(mydata3)

result = []
audience = soup.select('td.audience')
for i in audience:
  # result.append((i.text).replace('명\r\n','').rstrip())
  result.append((i.text).strip()[0:6])
mydata4 = result
# print(mydata4)

result = []
cumulative = soup.select('td.cumulative')
for i in cumulative:
  # result.append((i.text).replace('명\r\n','').rstrip())
  result.append((i.text).strip()[0:10])
mydata5 = result
# print(mydata5)

result = []
sale = soup.select('td.sales')
for i in sale:
  # result.append((i.text).replace('원\r\n','').rstrip())
  result.append((i.text).strip()[0:14])
mydata6 = result
# print(mydata6)

mycolumn = ['순위','제목','개봉일','관객수','누적관객수','누적매출액']

myframe = pd.DataFrame(data = list(zip(mydata1, mydata2, mydata3, mydata4, mydata5, mydata6)), columns = mycolumn)
myframe = myframe.set_index('순위')
# print(myframe)

filename = 'quiz_03_Movie.csv'
myframe.to_csv(filename, encoding='utf-8', index=False)
# print(filename, ' saved…', sep='')
# print('finished')

dfmovie = myframe.reindex(columns=['제목','관객수','누적관객수'])
# print(dfmovie)

mygroup0 = dfmovie['제목']
mygroup1 = dfmovie['관객수']
mygroup1 = mygroup1.str.replace(',','')
mygroup2 = dfmovie['누적관객수']
mygroup2 = mygroup2.str.replace(',','')


df = pd.concat([mygroup1, mygroup2], axis=1)
df = df.set_index(mygroup0)
df.columns = ['관객수','누적관객수']
print(df)

df.astype(float).plot(kind='barh',title ='영화별 관객수와 누적관객수', rot=0)
filename = 'quiz_03_MovieGraph.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
plt.show()

# df.astype(float).plot(kind='barh',title ='영화별 관객수와 누적관객수', rot=0)
# filename = 'quiz_03_MovieGraph.png'
# plt.savefig(filename, dpi=400, bbox_inches='tight')
# plt.show()
