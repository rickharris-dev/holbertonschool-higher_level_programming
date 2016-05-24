'''Function votes for id 1024 times'''

import requests

''' Counter and total votes count '''
i = 0
votes = 1024

''' URL and form data '''
url = 'http://173.246.108.142/level0.php'
form = {
    'id': '38',
    'holdthedoor': 'Submit'
}

''' Loop to submit requests '''
while i < votes:
    r = requests.post(url, data=form)
    i += 1
