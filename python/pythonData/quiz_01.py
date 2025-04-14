import numpy as np
from bs4 import BeautifulSoup
from pandas import DataFrame as df
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'NanumBarunGothic'

html = open('/work/neo/html/source/5/ex5-10.html', 'r', encoding='utf-8')
soup = BeautifulSoup(html, 'html.parser')
tbody = soup.select_one('tbody')
tds = tbody.find_all('td')

result =[]
for t in tds:
  result.append(t.text)
result = np.reshape(result, (4,3))
print(result)

mycolumns = ['이름','국어','영어']
myframe = df(data=result, columns=mycolumns)
myframe = myframe.set_index('이름')
print(myframe)


myframe.astype(float).plot(title='Score', kind='line', legend=True)

filename = 'quiz.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + ' saved')
plt.show()