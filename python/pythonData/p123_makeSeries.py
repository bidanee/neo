"""
pandas : 데이터를 다루기 위한 라이브러리로, 특히 표 형식의 데이터를 쉽게 처리하고 분석할 수 있게 해주는 도구. 데이터 분석에 많이 사용되며, DataFrame이라는 자료 구조를 제공해 데이터를 행(row)과 열(column)로 구성된 표 형태로 저장하고 조작할 수 있게 해준다.
"""

from pandas import Series

mylist = [10, 40, 30]
myindex = ['김유신', '이순신', '강감찬']

print('\n #Case 01')
myseries = Series(mylist)
print(myseries)

print('\n #Case 02')
myseries = Series(data=mylist)
print(myseries)

print('\n #Case 03')
myseries = Series(data=mylist, index=myindex)
print(myseries)

print('\n #Case 04')
myseries = Series(data=mylist, index=myindex, dtype=float)
print(myseries)