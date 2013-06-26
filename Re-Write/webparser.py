import urllib, urllib2, zipfile, sys, os, copy
from bs4 import BeautifulSoup

#Global Definitions

def dlProgress(count, blockSize, totalSize):
    percent = int(count*blockSize*100/totalSize)
    sys.stdout.write("\rDownload:...%d%%" % percent)
    sys.stdout.flush()

#Adobe

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
                plugin = td_tag[i].get_text()
        return windows, plugin

#java

#SuperAntiSpyware

#Ccleaner

