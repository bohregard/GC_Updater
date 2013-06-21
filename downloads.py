import urllib2, urllib, copy, sys
from bs4 import BeautifulSoup
from selenium import webdriver  
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.common.keys import Keys  

############################################
#Checks Text file to begin version compares#
############################################

def dlProgress(count, blockSize, totalSize):
    percent = int(count*blockSize*100/totalSize)
    sys.stdout.write("\r...%d%%" % percent)
    sys.stdout.flush()
        
class Downloads:
    
    def __init__(self):
        return

    def version_find(self, windows, firefox, java, core, trace):
        self = open('Downloads.txt', 'r')
        lines = []
        lines[:] = range(0,20)
        count = []
        count[:] = range(0,20)
        i = 0
        for line in self:
            lines[i] = line
            i += 1
        i = 0
        while lines[i] != '\n':
            if lines[i] == "Windows:\n":
                windows = lines[i+1]
                windows = windows.rstrip('\n')
                #print windows
            if lines[i] == "Firefox:\n":
                firefox = lines[i+1]
                firefox = firefox.rstrip('\n')
            if lines[i] == "Java:\n":
                java = lines[i+1]
                java = java.rstrip('\n')
            if lines[i] == "SAS Core:\n":
                core = lines[i+1]
                core = core.rstrip('\n')
            if lines[i] == "SAS Trace:\n":
                trace = lines[i+1]
                trace = trace.rstrip('\n')
            i += 1
        self.close
        return windows, firefox, java, core, trace

    def version_print(self):
        windows = ""
        firefox = ""
        java = ""
        trace = ""
        core = ""
        (windows, firefox, java, core, trace) = self.version_find(windows, firefox, java, core, trace)
        #print "Windows:", windows, "Firefox:", firefox
        return windows, firefox, java, core, trace

class JavaDownload:
    def __init__(self):
        browser = webdriver.Ie()  
        browser.get('http://java.com/en/download/manual.jsp')  
        html_source = browser.page_source
        browser.quit()
        #html = urllib2.urlopen("http://java.com/en/download/manual.jsp")
        #html = html.read()
        soup = BeautifulSoup(html_source)
        (java32,java64) = ('','')
        for link in soup.find_all(title='Download Java software for Windows Offline'):
            java32 = link.get('href')
        for link in soup.find_all(title='Download Java software for Windows (64-bit)'):
            java64 = link.get('href')
        urllib.urlretrieve(java32,"5 - Java_32.exe", reporthook=dlProgress)
        print "\nCompleted Java 32 bit Download"
        urllib.urlretrieve(java64,"5 - Java_64.exe", reporthook=dlProgress)
##        copy.CopyFiles("5 - Java_32.exe")
##        copy.CopyFiles("5 - Java_64.exe")
        return

class SuperDownload:
    def __init__(self):
        sasfile='http://www.superantispyware.com/downloads/temp/SAS_733093B.COM'
        urllib.urlretrieve(sasfile,"SAS.com",reporthook=dlProgress)
        return

class WriteDownloadsFile:

    def __init__(self, a, b, c,d,e):
        tobewritten = ['Windows:', a,'Firefox:',b,'Java:',c,'SAS Core:',d,'SAS Trace:',e,'\n']
        self = open('Downloads.txt', 'w')
        self.seek(0)
        for line in tobewritten:
            self.write(line + '\n')
        self.seek(0)
        #self.read()
        self.close
        return
