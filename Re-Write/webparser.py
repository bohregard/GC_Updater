from bs4 import BeautifulSoup

#Global Definitions

#Adobe

class AdobeUpdater:
    def __init__(self):
        return

    def adobe_version(self):
        return

#java

#SuperAntiSpyware

#Ccleaner

class Updater:
    def __init__(self):
        return
    def web_update(self):
        with open('downloads.html','r') as f:
            read = f.read()

        html = BeautifulSoup(read)
        p = html.find_all('p')
        for i in range(len(p)):
            p[i] = p[i].get_text()
            p[i] = p[i].strip('JavaAdobePluginActiveXSASCoreTraceCcleaner: ')

        for line in p:
            print line
        return p
