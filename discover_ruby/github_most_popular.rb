require 'httpclient'
require 'json'

extheaders = {
  'User-Agent' => 'Holberton_School',
  'Authorization' => 'token 4d55fa9beb614fd08ed010f0442c5a7239e734ee'
}

uri = "https://api.github.com/search/repositories?q=language:ruby&sort=stars&order=desc"

clnt = HTTPClient.new
puts clnt.get_content(uri, extheaders)
