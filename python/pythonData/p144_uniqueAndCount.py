from pandas import Series

print('\n Unique and Count and isin')
mylist = ['라일락', '코스모스', '백일홍', '코스모스', '코스모스', '들장미', '들장미', '라일락', '라일락']
myseries = Series(data = mylist)
print(myseries)

# uinique : 나는 하나다 , 중복없이 고유값만 뽑아줌
print('\n unique')
myunique = myseries.unique()
print(myunique)
print('-'*50)

print('\n value_counts()')
mycount = myseries.value_counts()
print(mycount)
print('-'*50)

# isin : 안에있니 있으면 True 아니면 False
print('\n isin')
mask = myseries.isin(['들장미', '라일락'])
print(mask)
print('-'*50)

# mask : 필터 조건 , myseries[mask]는 True인 값들만 출력해줌.
print(myseries[mask])
print('-'*50)
print('Done')
