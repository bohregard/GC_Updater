import urllib, urllib2
from bs4 import BeautifulSoup

class AdobeUpdater:
    def __init__(self):
        return

    def adobe_version(self):
        #Open url and find td tags containing versions
        url = urllib2.urlopen("http://www.adobe.com/software/flash/about/")
        html = url.read()
        soup = BeautifulSoup(html)
        td_tag = soup.find_all('td')

        iTerator = []
        iTerator[:] = range(2,16)

        for i in iTerator:
            if i == 2:
                windows = td_tag[i].get_text()
            if i == 6:
                firefox = td_tag[i].get_text()
        return windows, firefox

class JavaUpdater:
    def __init__(self):
        return

    def java_check(self):
        #Check for latest versions of Java using BS
        url = urllib2.urlopen("http://java.com/en/download/chrome.jsp?locale=en")
        html = url.read()
        soup = BeautifulSoup(html)
        b_tag = soup.find_all('b')
        return b_tag[0].get_text()
