import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'NanumBarunGothic'

filename = 'ex802.csv'
myframe = pd.read_csv(filename, index_col='type' , encoding='utf-8')
print(myframe)

myframe.plot(title='Some Title', kind='line', rot=0, legend=True)

filename = 'Ex_p239_dataframeGraph01.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + ' saved')
plt.show()