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

    
class SuperAntiUpdater:
    def __init__(self):
        return
    def sas_check(self):
        url = urllib2.urlopen('http://www.superantispyware.com/definitions.html')
        html = BeautifulSoup(url)
        td_tag = html.find_all("td",align='center')
        for i in range(len(td_tag)):
            #print i, "=",td_tag[i].get_text()
            if td_tag[i].get_text() == 'Core Definitions':
                #print td_tag[i+1].get_text(),"Found successful"
                core_Def = td_tag[i+1].get_text()
            if td_tag[i].get_text() == 'Trace Definitions':
                #print td_tag[i+1].get_text(),"Found successful"
                trace_Def = td_tag[i+1].get_text()
        #print "Core Definitions:",core_Def,"\nTrace Defintions:",trace_Def
        return core_Def, trace_Def
(a,b) = SuperAntiUpdater().sas_check()
