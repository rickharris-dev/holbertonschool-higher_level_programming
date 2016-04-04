import urllib2
import json

request_headers = {
  'Content-Type': 'application/json',
  'User-Agent': 'Holberton_School',
  'Authorization': 'token 4d55fa9beb614fd08ed010f0442c5a7239e734ee'
}
url = "https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc"
array = []
req = urllib2.Request(url, headers=request_headers)
response = urllib2.urlopen(req)
data = json.load(response)
for i in data['items']:
    user_url = i['owner']['url']
    user_req = urllib2.Request(user_url, headers = request_headers)
    user_response = urllib2.urlopen(user_req)
    user_data = json.load(user_response)
    array.append(dict([('full_name', i['full_name']), ('location', user_data['location'])]))
print json.dumps(array)
