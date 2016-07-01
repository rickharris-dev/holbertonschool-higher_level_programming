import threading
import requests
import json

class IPThread(threading.Thread):

    def __init__(self, ip, callback):
        threading.Thread.__init__(self)
        self.__ip = ip
        self.__callback = callback

    def run(self):
        url = 'https://api.ip2country.info/ip?' + str(self.__ip)
        print("Search: " + self.__ip)
        res = requests.get(url)
        data = json.loads(res.text)
        self.__callback(data['countryName'])
        print("countryName: " + data['countryName'])
