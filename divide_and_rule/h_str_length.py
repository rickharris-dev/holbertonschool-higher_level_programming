import threading

class StrLengthThread(threading.Thread):

    total_str_length = 0

    def __init__(self, word):
        threading.Thread.__init__(self)
        if type(word) != str:
            raise Exception("word is not a string")
        self.__word = word

    def run(self):
        StrLengthThread.total_str_length += len(self.__word)
