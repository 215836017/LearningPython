import urllib.request

response = urllib.request.urlopen("https://baike.baidu.com/item/Python/407313?fr=aladdin")  # type:urllib.response

# print(response.read().decode('utf-8'))
print(type(response))
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))
print('code=', response.code)
print('version=', response.version)
