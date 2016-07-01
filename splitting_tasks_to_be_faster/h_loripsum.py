import threading
import requests
import logging

class LoripsumThread(threading.Thread):

    lock = threading.Lock()

    def __init__(self, filename):
        threading.Thread.__init__(self)
        self.__filename = filename

    def run(self):
        url = 'http://loripsum.net/api/1/short'
        res = requests.get(url)
        LoripsumThread.lock.acquire()
        try:
            f = open(self.__filename, 'a')
            f.write(res.text.encode('utf-8'))
            f.close()
        finally:
            LoripsumThread.lock.release()
