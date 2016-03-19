require 'httpclient'
require 'json'

extheaders = {
  'User-Agent' => 'Holberton_School',
  'Authorization' => 'token 4d55fa9beb614fd08ed010f0442c5a7239e734ee'
}
filename = '/tmp/38'
uri = "https://api.github.com/search/repositories?q=language:ruby&sort=stars&order=desc"
target = open(filename,'w')
target.truncate(0)
clnt = HTTPClient.new

res = clnt.get_content uri, extheaders
target.write(res)
puts "The file was saved!"
target.close
