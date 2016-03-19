require 'httpclient'
require 'json'
require 'thread'

extheaders = {
  'User-Agent' => 'Holberton_School',
  'Authorization' => 'token 4d55fa9beb614fd08ed010f0442c5a7239e734ee'
}

query = {
  'q' => 'language:ruby',
  'sort' => 'stars',
  'order' => 'desc'
}

uri = "https://api.github.com/search/repositories"

clnt = HTTPClient.new
json_string = clnt.get_content(uri, query, extheaders)
res = JSON.parse(json_string)['items']
list = Array.new
threads = []
names = res.map do |e|
  owner_uri = e["owner"]["url"]
  owner_query = {'q' => 'language:ruby'}
  threads << Thread.new(owner_uri, owner_query, extheaders, e['full_name']) do |url, query, extheaders, full_name|
    owner_json = clnt.get_content(url, query, extheaders)
    owner_res = JSON.parse(owner_json)
    new_element = {
      'full_name' => e['full_name'],
      'location' => owner_res['location']
    }
    list.push(new_element)
  end
end

threads.each { |thr| thr.join }
puts list.to_json
