#!/usr/bin/env python3

dictionary = {'이단비' : 24, '정민아' : 15, '주서연': 13}
print('Dictionary :', dictionary)

for key in dictionary.keys():
  print(f'key : {key}')

for value in dictionary.values():
  print(f'value : {value}')

for key in dictionary.keys():
  print('{}의 나이는 {}입니다.'.format(key, dictionary[key]))

for key,value in dictionary.items():
  print(f'{key}의 나이는 {value}입니다.')

findKey = ('서예린')

if findKey in dictionary.keys():
  print(f'{findKey}(은)는 존재합니다.')
else:
  print(f'{findKey}(은)는 존재하지 않습니다.')

result = dictionary.pop('주서연')
print('After pop : ', dictionary)
print('Result : ', result)

dictionary.clear()
print('Dictionary list : ', dictionary)

