import requests
import json

url1 = 'https://postman-echo.com/digest-auth'
headers1 = {'Authorization': 'Digest username="postman", realm="Users", nonce="ni1LiL0O37PRRhofWdCLmwFsnEtH1lew", uri="/digest-auth", response="254679099562cf07df9b6f5d8d15db44", opaque=""'}
params = {'있으면': '이런식으로'}
data1 = {'이것도있읍면': '이런식으로'}

response = requests.get(url1, headers=headers1)
# post예시 response = requests.post(url1, headers=headers1, params=params,data=json.dumps(data1))

print(response.status_code)
print(response.url)
print(response.headers)
print(response.content)
