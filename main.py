import urllib


import urllib.request


class ProfanityChecker(object):
    def __init__(self):
        self.url = "http://www.wdylike.appspot.com/?q="

    def read_from_file(self):
        quotes = open("text_file.txt")
        content = quotes.read()
        quotes.close()
        self.check_profanity(content)

    def check_profanity(self,text_to_check):
        connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check)
        output = connection.read()
        print(output)
        connection.close


if __name__ == '__main__':
    profanitychecker = ProfanityChecker()
    profanitychecker.read_from_file()
