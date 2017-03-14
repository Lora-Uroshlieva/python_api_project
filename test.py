import requests

url = 'http://requestb.in/1ed1jev1'
json = {
    'month': "May",
    'result': "1-0",
    'team': "manchester"
}
response = requests.post(url, params=json)
print(response.status_code)
print(response.content)


url_2 = 'http://httpbin.org/'
params = {
    'id': [1, 2, 3, 4],
}
r = requests.get(url_2, params=params)
print(r)

