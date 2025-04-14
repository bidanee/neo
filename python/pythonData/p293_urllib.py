import urllib.request

url = "https://shared-comic.pstatic.net/thumb/webtoon/648419/thumbnail/thumbnail_IMAG10_1421195d-13be-4cde-bcf9-0c78d51c5ea3.jpg"

savename = 'p293_urldownload.jpg'

result = urllib.request.urlopen(url)

data = result.read()
print('#type : ', type(data))

with open(savename, 'wb') as f:
  f.write(data)
  print(savename + ' saved')