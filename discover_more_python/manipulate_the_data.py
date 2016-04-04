import urllib2
import json
from pprint import pprint

request_headers = {
  'Content-Type': 'application/json',
  'User-Agent': 'Holberton_School',
  'Authorization': 'token 4d55fa9beb614fd08ed010f0442c5a7239e734ee'
}
url = "https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc"

req = urllib2.Request(url, headers=request_headers)
response = urllib2.urlopen(req)
data = json.load(response)
for i in data['items']:
    print i['full_name']
